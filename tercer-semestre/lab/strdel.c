#include <stdio.h>
#include <string.h>
#define LARGO 100

int *modificarstr(char *str);

int main () {
    char str[LARGO];
    printf("Ingresa frase: ");
    fgets(str, LARGO, stdin);

    modificarstr(str);

    printf("%s", str);

    return 0;
}

int *modificarstr(char *str) {

    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] == ' ' || str[i] == '\t') {
            // Correr todo a la izquierda desde i
            while (str[i] != '\0') {
                str[i] = str[i + 1];
                i++;
            }
            i = -1;
        }
    }

    return 0;
}

/*  Alternativa 1
int main() {
    char c = getc(stdin); 
    while (c != '\n') {
        if (c != ' ' && c != '\t') {
            printf("%c", c);
        }
        c = getc(stdin);
    }
    printf("\n");
    return 0;
} */