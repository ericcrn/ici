#include <stdio.h>
#include <math.h>

int es_primo(int n);

int main() {
    int n;

    printf("Ingrese un número: ");
    scanf("%d", &n);

    int contador = 0;
    for(int i = 0; i < n; i++) {
        if (es_primo(i)) {
            contador++;
            printf("[%d] ", i);
        }
    }
    printf("\n Primos totales: %d\n", contador);
    return 0;
}

int es_primo(int n) {
    if (n <= 1) {
        return 0;
    }
    else if (n == 2 || n == 3) {
        return 1;
    }
    else if (n % 2 == 0) {
        return 0;
    }
    else {
        for (int i = 3;  i <= (sqrt(n)); i++) {
            if (n % i == 0) {
                return 0; 
            }
        }
    }
    return 1; 
}