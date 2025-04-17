#include <stdio.h>
#define N 2
#define M 4

void generartraspuesta(int original[N][M], int traspuesta[M][N]);

int main() {
    int original[N][M], traspuesta[M][N];
    int i, j;
    int contador = 1;

    printf("Generando matriz original de %d filas y %d columnas:\n\n", N, M);
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            original[i][j] = contador;
            contador++;
        }
    }

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            printf("%d\t", original[i][j]);
        }
        printf("\n");
    }

    printf("\n\nLa matriz traspuesta es: \n\n");
    generartraspuesta(original, traspuesta);

    for (i = 0; i < M; i++) {
        for (j = 0; j < N; j++) {
            printf("%d\t", traspuesta[i][j]);
        }
        printf("\n");
    }

    return 0;
}

void generartraspuesta(int original[N][M], int traspuesta[M][N]) {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            traspuesta[j][i] = original[i][j];
        }
    }
}