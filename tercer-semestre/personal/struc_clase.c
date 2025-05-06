#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX_CARTAS 52
#define MAX_MANO 12

// Estructura de una carta
typedef struct {
    char *nombre;
    int valor;
} Carta;

// Estructura de un jugador
typedef struct {
    Carta mano[MAX_MANO];
    int total;
    int num_cartas;
} Jugador;

// Mazo
Carta mazo[MAX_CARTAS];

// Funciones
void inicializarMazo();
void barajar();
Carta repartirCarta(int *indice_mazo);
void agregarCarta(Jugador *j, Carta c);
void mostrarMano(Jugador *j, const char *nombre);
int calcularTotal(Jugador *j);
int esBlackjack(Jugador *j);

int main() {
    srand(time(NULL));
    inicializarMazo();
    barajar();

    Jugador jugador = {{0}, 0, 0};
    Jugador dealer = {{0}, 0, 0};
    int indice_mazo = 0;

    // Repartir cartas iniciales
    agregarCarta(&jugador, repartirCarta(&indice_mazo));
    agregarCarta(&dealer, repartirCarta(&indice_mazo));
    agregarCarta(&jugador, repartirCarta(&indice_mazo));
    agregarCarta(&dealer, repartirCarta(&indice_mazo));

    // Mostrar mano inicial
    mostrarMano(&jugador, "Jugador");
    printf("Carta visible del Dealer: %s\n\n", dealer.mano[0].nombre);

    // Turno del jugador
    char opcion;
    while (1) {
        printf("¿Deseas pedir otra carta? (s/n): ");
        scanf(" %c", &opcion);

        if (opcion == 's' || opcion == 'S') {
            agregarCarta(&jugador, repartirCarta(&indice_mazo));
            mostrarMano(&jugador, "Jugador");

            if (jugador.total > 21) {
                printf("¡Te pasaste! Pierdes.\n");
                return 0;
            }
        } else {
            break;
        }
    }

    // Turno del dealer
    mostrarMano(&dealer, "Dealer");
    while (dealer.total < 17) {
        agregarCarta(&dealer, repartirCarta(&indice_mazo));
        mostrarMano(&dealer, "Dealer");
    }

    // Resultados
    if (dealer.total > 21 || jugador.total > dealer.total) {
        printf("¡Ganaste!\n");
    } else if (jugador.total < dealer.total) {
        printf("Perdiste.\n");
    } else {
        printf("Empate.\n");
    }

    return 0;
}

// Implementaciones
void inicializarMazo() {
    const char *nombres[] = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
    int valores[] = {11,2,3,4,5,6,7,8,9,10,10,10,10};
    int index = 0;

    for (int i = 0; i < 4; i++) { // 4 palos
        for (int j = 0; j < 13; j++) {
            mazo[index].nombre = strdup(nombres[j]);
            mazo[index].valor = valores[j];
            index++;
        }
    }
}

void barajar() {
    for (int i = 0; i < MAX_CARTAS; i++) {
        int j = rand() % MAX_CARTAS;
        Carta temp = mazo[i];
        mazo[i] = mazo[j];
        mazo[j] = temp;
    }
}

Carta repartirCarta(int *indice_mazo) {
    return mazo[(*indice_mazo)++];
}

void agregarCarta(Jugador *j, Carta c) {
    j->mano[j->num_cartas++] = c;
    j->total = calcularTotal(j);
}

void mostrarMano(Jugador *j, const char *nombre) {
    printf("%s: ", nombre);
    for (int i = 0; i < j->num_cartas; i++) {
        printf("%s ", j->mano[i].nombre);
    }
    printf("=> Total: %d\n", j->total);
}

int calcularTotal(Jugador *j) {
    int total = 0;
    int ases = 0;

    for (int i = 0; i < j->num_cartas; i++) {
        total += j->mano[i].valor;
        if (j->mano[i].valor == 11) ases++;
    }

    while (total > 21 && ases > 0) {
        total -= 10;
        ases--;
    }

    return total;
}