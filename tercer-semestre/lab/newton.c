#include <stdio.h>

float iteracion(float g_n, float n);
float valor_absoluto(float numero);

int main() {
    float n;
    printf("Ingrese numero que desea encontrar su raiz: ");
    scanf("%f", &n);

    float g_n = (n / 2), g_n1 = iteracion(g_n, n), g_temp;

    while (valor_absoluto((g_n1 - g_n)) > 0.000001) {
        g_n = g_n1;
        g_n1 = iteracion(g_n, n);
    }
    
    printf("La raiz de %f es %f", n, g_n1);

    return 0;
}

float iteracion(float g_n, float n) {
    float g_n1 = (g_n + (n / g_n)) / 2;

    return g_n1;
}

float valor_absoluto(float numero) {
    if (numero < 0.0) {
        return -numero;
    } else {
        return numero;
    }
}