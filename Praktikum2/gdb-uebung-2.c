#include <stdio.h>

int f(int a, int b) {
  return 3*a + 7*b;
}

int g(int a, int b) {
  return 10*a*a - 3*b;
}

int h(int a, int b) {
  return a + b + 300;
}

int main() {
  int a = 5, b=9, c=0;

  c = f(g(a,h(a,b)),h(b,a));

  printf("a = %d, b = %d, c = %d\n", a, b, c);
}
