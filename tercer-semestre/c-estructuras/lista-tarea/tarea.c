#include <stdio.h>
#include <stdlib.h>
#include "pila.h"



int leerdatos(char *dir, TipoPila *Pila){
    FILE *archivo = fopen(dir, "r");
    if (archivo == NULL) {
        perror("Error al abrir el archivo");
        return 0;
    }

    int num;
    char letra;


    while (fscanf(archivo, "%d,%c", &num, &letra) == 2) {
        printf("Leido -> Numero: %d Letra: %c\n", num, letra);

        *Pila = insertarTope(*Pila, num, letra);
    }

    fclose(archivo);

    return 0;
}

int agregar(char *dir, int cantidad, TipoPila *Pila) {
    FILE *archivo = fopen(dir, "r");
    if (archivo == NULL) {
        perror("Error al abrir el archivo");
        return 0;
    }

    int num;
    char letra;

    for (int i = 0; i < cantidad; i++) {
        if (fscanf(archivo, "%d,%c", &num, &letra) == 2) {
            printf("Agregado a la Pila -> Numero: %d Letra: %c\n", num, letra);

            *Pila = insertarTope(*Pila, num, letra);
        }
    }

    fclose(archivo);

    return 0;
}

int imprimirPila(TipoPila *Pila) {
    TipoPila actual = *Pila; 
    printf("\n\nIMPRESIÓN DE PILA:\n");

    while (actual != NULL) {
        printf("%d\t%c\n", actual->num, actual->letra);
        actual = actual->siguiente;
    }
    
    return 0;
}


int main() {
    TipoPila Pila = crearPila();

    leerdatos("datos.txt", &Pila);
    leerdatos("datos1.txt", &Pila);
    

    if (Pila == NULL) {
        printf("La pila está vacía.\n");
    } else {
        printf("Tope de Pila -> Numero: %d Letra: %c\n", Pila->num, Pila->letra);
    }

    for (int i = 0; i < 3; i++) {
        Pila = borrarTope(Pila);
        printf("Tope de Pila eliminado.\n");
    }
    printf("NUEVO Tope de Pila -> Numero: %d Letra: %c\n", Pila->num, Pila->letra);

    agregar("datos.txt", 2, &Pila);
    imprimirPila(&Pila);

    return 0;
}