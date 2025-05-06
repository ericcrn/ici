#include <stdlib.h>
#include "pila.h"


TipoPila crearPila() {
    return NULL; // retorna nulo
} 

TipoPila insertarTope(TipoPila lista, int num, char letra) {
    TipoPila nuevoNodo = malloc(sizeof(struct Nodo)); //a nuevoNodo(puntero de estructura Nodo) se le asigna un espacio de memoria
    nuevoNodo->num = num; //a la variable num de nuevoNodo se le asigna un numero
    nuevoNodo->letra = letra; //a la variable letra de nuevoNodo se le asigna una nueva letra
    nuevoNodo->siguiente = lista; // al puntero que apunta al siguiente Nodo se le asigna la lis

    return nuevoNodo; //se retorna el nuevoNodo con el nuevo tope.
}

TipoPila borrarTope(TipoPila lista) { 
    if (lista == NULL) return NULL; // Si la pila esta vacia (no hay nodos) devuelve null, indicando que estta

    TipoPila aux = lista->siguiente; // Guarda una referencia del segundo nodo de la pila.
    free(lista); // Libera la memoria ese nodo.

    return aux; // Devuelve el nodo que estaba despues del que se elimino, siendo este el nuevo nodo.
}

TipoPila borrarPila(TipoPila lista) {
    TipoPila aux;
    
    while (lista != NULL) {
        aux = lista->siguiente;
        free(lista);
        lista = aux;
    }

    return NULL;
}

int esPilaVacia(TipoPila p) {
    return p == NULL;
}

TipoPila verTopePila(TipoPila lista) {
    if (lista != NULL) return lista;
    
    return NULL;
}