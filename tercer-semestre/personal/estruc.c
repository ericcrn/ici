#include <stdio.h>

struct weones {
    char nombre[50];
    char apellido[50];
    int nivel_weon;
    int fantasmometro;
};

int main() {
    struct weones williams = {"williams", "campos", 10, 100};
    printf("nombre: %s \napellido: %s \nnivel de weon (1-10): %d \nnivel de fantasma (1-100): %d\n", williams.nombre, williams.apellido, williams.nivel_weon, williams.fantasmometro); 

    struct weones *pwilliams = &williams;
    printf("nombre: %s \napellido: %s \nnivel de weon (1-10): %d \nnivel de fantasma (1-100): %d\n", pwilliams -> nombre, pwilliams -> apellido, pwilliams -> nivel_weon, pwilliams -> fantasmometro); 
    
}
