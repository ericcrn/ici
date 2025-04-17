#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int maxIndex = n - 1;
    while (maxIndex > 0) {
        int lastSwap = 0; // Índice del último intercambio
        for (int j = 0; j < maxIndex; j++) {
            if (arr[j] > arr[j + 1]) {
                // Intercambiar arr[j] y arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                lastSwap = j;
            }
        }
        maxIndex = lastSwap; // Reducir el rango de comparación
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Array original: \n");
    printArray(arr, n);

    bubbleSort(arr, n);

    printf("Array ordenado: \n");
    printArray(arr, n);

    return 0;
}