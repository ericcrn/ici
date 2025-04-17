#include <stdio.h>

int main() {
    char palabra[] = "puntero";
    char *ppalabra = &palabra;

    printf("%p\n", ppalabra);        // Dirección de inicio
    printf("%c\n", *ppalabra);       // 'p'
    printf("%c\n", *(ppalabra + 3)); // 't'
    return 0;
}