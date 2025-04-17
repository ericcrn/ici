#include <stdio.h>
#define N 3

int main() {
    float M[N][N];
    float F[N][N];
    float L[N][N];
    int i, j;

    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++) {
            M[i][j] = 0;
            F[i][j] = 0;
            L[i][j] = 0;
        }
    }
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            scanf("%f", &M[i][j]);
        }
    }
}