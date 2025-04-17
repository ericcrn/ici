/*Dos números a y b se dice que son amigos si la suma de los divisores
de a (sin considerarse a sí mismo) coincide con b y viceversa.
Programar en C, un algoritmo que tenga como entrada dos números
naturales Num1 y Num2, muestre en pantalla todas las parejas de
números amigos que existan en el intervalo determinado por Num1
y Num2.*/

#include <stdio.h>

int es_amigo(int a, int b);
int sum_divisores(int n);

int main() {
    int num1, num2;
    printf("Introduzca el intervalo [ej: 0 5000]: ");
    scanf("%d %d", &num1, &num2);

    for (int i = num1; i < num2; i++) {
        for (int j = i+1; j < num2; j++) {
            if (es_amigo(i, j) == 1) {
                printf("Pareja encontrada: (%d, %d)\n", i, j);
            }
        }
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

int es_amigo(int a, int b) {
    int i = 1, sum_a = sum_divisores(a), sum_b = sum_divisores(b);

    if ((sum_a == b) && (sum_b == a)) {
        return 1;
    } else {
        return 0;
    }
}