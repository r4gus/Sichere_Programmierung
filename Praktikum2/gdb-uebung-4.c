#include <stdio.h>

int main() {
    int anzahl;
    float summe;
    float i;

    summe = 0, anzahl = 0;
    for (i = 1000; i <= 1000.03; i += .01) {
        summe += i;
        anzahl++;
    }
    printf("Summe: %f, Anzahl: %d\n", summe, anzahl);

    return 0;
}
