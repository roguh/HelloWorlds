#include <stdlib.h>
#include <stdio.h>


int main() {
  int* mem = malloc(0xffffffffff);
  printf("bye %c\n", mem[0]);
  return 1;
}
