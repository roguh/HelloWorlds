#include <stdio.h>

int main(int argc, char** argv)
{
  printf("Hello, world!\n");

  // Print each command-line argument
  for (int i = 1; i < argc; i++) {
    printf("%s\n", argv[i]);
  }

  return 0;
}
