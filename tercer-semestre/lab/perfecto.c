#include <stdio.h>
#define CANT 4

int sum_divisores(int n);

int main() {
    int snumperfecto = 0, i = 0; 

for (i = 1; snumperfecto < (CANT + 1); i++) {
        if (sum_divisores(i) == i) {
            printf("Se encontro un num perfecto: %i\n", i);
            snumperfecto += 1;
        }
    }

    return 0;
}

int sum_divisores(int n) {
    int i = 1, sum = 0;

    while (i <= (n/2)) { // Dividimos en 2 porque despues de la mitad del num el unico divisor es el mismo num.
        if ((n % i) == 0) {
            sum += i;
        }
        i++;
    }
    return sum;
}