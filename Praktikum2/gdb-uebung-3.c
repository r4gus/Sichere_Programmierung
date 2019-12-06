#include <stdio.h>

unsigned int f(unsigned int i) {
  if (i>1) {
    return i * f(i-1);
  } else {
    return 1;
  }
}

int main() {
  unsigned int i=5, r=0;

  r = f(i);

  printf("i = %d, f(i) = %d\n", i, r);
}
