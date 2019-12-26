#include <dirent.h>
#include <pwd.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <time.h>
#include <unistd.h>

#define ERR_MSG(x) "ERROR (" x ")"

int strcoll_comp(const struct dirent** a, const struct dirent** b) {
  return strcoll((*a)->d_name, (*b)->d_name);
}

int main(int argc, char** argv)
{
  // no ls equivalent...
  bool print_full = false;
  // -a
  bool print_attrs = true;
  // -F
  bool print_type = true;
  // -a
  bool print_hidden = true;

  char* target_dir;
  if (argc > 1) {
    target_dir = argv[1];
  } else {
    target_dir = ".";
  }

  if (chdir(target_dir)) {
    perror(ERR_MSG("chdir"));
    return -1;
  }

  long cwd_len = pathconf(target_dir, _PC_PATH_MAX);
  char* cwd = malloc(cwd_len);
  if (!cwd) {
    perror(ERR_MSG("malloc"));
  }

  if (!getcwd(cwd, cwd_len)) {
    perror(ERR_MSG("getcwd"));
    return -1;
  }

  struct dirent** namelist;
  int n = scandir(cwd, &namelist, NULL, strcoll_comp);
  if (n == -1) {
    perror(ERR_MSG("scandir"));
    return -1;
  }

  while (n--) {
    struct dirent* d = namelist[n];

    bool is_up = strcmp(d->d_name, ".") == 0 || strcmp(d->d_name, "..") == 0;
    bool is_hidden = !is_up && d->d_name[0] == '.';

    if (is_up || (!print_hidden && is_hidden)) {
      free(d);
      continue;
    }

    struct stat st;

    if ((print_attrs || print_type) && lstat(d->d_name, &st)) {
      perror(ERR_MSG("lstat"));
      return -1;
    }

    if (print_attrs) {
      struct passwd* pw;
      pw = getpwuid(st.st_uid);

      if (!pw) {
        perror(ERR_MSG("getpwuid"));
        return -1;
      }

      size_t max_time_len = 1024;
      char* t = malloc(max_time_len);
      struct tm* tt = localtime(&st.st_mtime);
      strftime(t, max_time_len, "%d %b %Y %I:%M", tt);

      printf("%03u  ", st.st_mode & 0xFFF);
      printf("%s  ", pw->pw_name);
      printf("%s  ", t);
    }

    if (print_full) {
      printf("%s/", cwd);
    }
    printf("%s", d->d_name);
    if (print_type) {
      if (S_ISDIR(st.st_mode)) {
        printf("/");
      } else if (S_IXUSR & st.st_mode) {
        printf("*");
      }

      if (S_ISLNK(st.st_mode)) {
        char* realp = realpath(d->d_name, NULL);

        if (realp == NULL) {
          perror(ERR_MSG("realpath"));
          return -1;
        }

        printf(" -> %s", realp);
      }
    }
    printf("\n");
    free(d);
  }

  free(namelist);
  free(cwd);
  return 0;
}
