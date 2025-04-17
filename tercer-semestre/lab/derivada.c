// Eric Cerna L. 22127660-4
#include <stdio.h>

int main() {
    float c1, c2, c3, c4, derivada;
    printf("Ingrese los coeficientes del polinomio en orden [ej:1 3 5 3]:");
    scanf("%f %f %f %f", &c1, &c2, &c3, &c4);
    printf("\nEl polinomio que ingreso es: %.2f + %.2fx + %.2fx^2 + %.2fx^3\n", c1, c2, c3, c4);

    c3 = c3 * 2;
    c4 = c4 * 3;

    printf("Su derivada es: %.2f + %.2fx + %.2fx^2\n", c2, c3, c4);

    return 0;
}
