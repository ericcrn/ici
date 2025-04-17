/* Realizar un programa en C, tal que permita determinar si un número natural N ingresado por teclado es primo o no. */

#include <stdio.h>
#include <math.h>

int main() {
    int n;
    printf("Ingrese el número que desea saber si es primo: ");
    scanf("%d", &n);

    if (n <= 1) {
        printf("No es primo.\n");
    }
    else if (n == 2 || n == 3) {
        printf("Es primo.\n");
    }
    else if ( (n % 2) == 0) {
        printf("No es primo.\n");
    }
    else {
        int es_divisible = 0;
        for (int i = 5; i <= sqrt(n); i++) {
            if ((n % i) == 0) {
                printf("Es divisible con %d\n", i);
                es_divisible = 1;
            }
            if ((i == (int)sqrt(n) && es_divisible == 1)) {
                printf("No es primo.\n");
                return 0;
            }

        }
        printf("Si es primo.\n");

        return 1;
    }

    return 0;
}