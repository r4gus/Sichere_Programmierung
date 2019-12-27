#include <stdio.h>
#include <string.h>

void print(char* s) {
    char buffer[200];

    strcpy(buffer, s);
    printf("Anfang von buffer: %p\n", buffer);
    printf("Inhalt von buffer: %s\n", buffer);
}

int main(int argc , char ** argv) {
    if (argc == 2) {
        print(argv [1]);
    } else {
        printf("Bitte ein Argument übergeben .\n");
    }

    return 0;
}
