/*Programar en C un algoritmo que sea capaz de determinar si un
número es perfecto o no. Un número es perfecto si la suma de sus
divisores entrega como resultado el mismo número.*/
#include <stdio.h>

int sum_divisores(int n);

int main() {
    int n;
    printf("Ingrese num: ");
    scanf("%d", &n);

    if (sum_divisores(n) == n) {
        printf("Es un numero perfecto!\n");
    } else {
        printf("No es perfecto.\n");
    }
    return 0;
}

int sum_divisores(int n) {
    int i = 1, sum = 0;

    while (i <= (n/2)) {
        if ((n % i) == 0) {
            sum += i;
        }
        i++;
    }
    return sum;
}