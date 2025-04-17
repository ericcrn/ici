/* Realizar un programa en C, tal que resuelva la conjetura de Collatz,
método matemático iterativo que propone la convergencia de un
número N al valor 1:
Las reglas para cada iteración, son las siguientes:
● Si el número es par, se divide entre 2 y el resultado reemplaza al
número N.
● Si el número es impar, se multiplica por 3, se incrementa en 1 y el
resultado reemplaza al número N. */

#include <stdio.h>

int main() {
    int n;
    printf("Ingrese N: ");
    scanf("%d", &n);

    while (n != 1) {
        if ((n % 2) == 0) {
            n = n / 2;
        } else {
            n = (n * 3) + 1;
        }
        printf("%d\n", n);
    }
    printf("FIN.\n");

    return 0;
}