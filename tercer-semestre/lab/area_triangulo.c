// Eric Cerna L. 22127660-4
#include <stdio.h>

float calculo_area(float b, float a);

int main() {
    float base = 0, altura = 0;
    printf("Ingrese la base y la altura con el siguiente formato: base altura\n");
    scanf("%f %f", &base, &altura);

    float resultado = calculo_area(base, altura);
    printf("El resultado del area es %.2f cm cuadrados", resultado);
    return 0;
}

float calculo_area(float b, float a) {
    float area = (b*a)/2;
    return area;
}