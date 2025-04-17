#include <stdio.h>
#define N 2
#define M 4

int ftraspuesta(int matriz[N][M], int traspuesta[M][N]);

int main() {
    // generamos la matriz
    int matriz[N][M];
    int traspuesta[M][N];
    int i, j, count = 1;

    printf("Se genero la siguiente matriz de %d filas y %d columnas:\n\n", N, M);
    
    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            matriz[i][j] = count; // inicializamos
            count++;
            printf("%d\t", matriz[i][j]);  // imprimimos 
        }
        printf("\n");
    }

    printf("\n\nSu matriz traspuesta es: \n\n");
    ftraspuesta(matriz, traspuesta); // generamos la traspuesta

    for (i = 0; i < M; i++) {
        for (j = 0; j < N; j++) {
            printf("%d\t", traspuesta[i][j]);  // imprimimos 
        }
        printf("\n");
    }


}

int ftraspuesta(int matriz[N][M], int traspuesta[M][N]) { // pasamos una matriz la cual vamos a modificar para no trabajar con punteros
    int i, j;

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            traspuesta[j][i] = matriz[i][j]; // invertimos i j por j i 
        }
    }

    return 0;
}