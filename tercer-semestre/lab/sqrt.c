// Eric Cerna L. 22127660-4
#include <stdio.h>
#include <math.h>

int main() {
    float num, raiz;
    printf("Ingrese el numero para calcular su raiz: \n");
    scanf("%f", &num);

    raiz = sqrt(num);
    printf("La raiz de %.2f, es %.2f.\n", num, raiz);

    return 0;
}