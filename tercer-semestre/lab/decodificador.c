#include <stdio.h>
#include <string.h>
#define PALABRA "MURCIELAGO"
#define LARGO 100

int main() {
    char str[LARGO];

    printf("Ingrese la frase: \n");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';

    size_t len = strlen(str);
    if (len > LARGO) {
        printf("La frase es demasiado larga.\n");
        return 1;
    }


    for (int i = 0; i < (len + 1); i++) {
        int letra = str[i];
        switch (letra) {
        
        case '0':
            str[i] = PALABRA[0];
            break;
        case '1':
            str[i] = PALABRA[1];
            break;
        case '2':
            str[i] = PALABRA[2];
            break;
        case '3':
            str[i] = PALABRA[3];
            break;
        case '4': 
            str[i] = PALABRA[4];
            break;
        case '5':
            str[i] = PALABRA[5];
            break;
        case '6':
            str[i] = PALABRA[6];
            break;
        case '7':
            str[i] = PALABRA[7];
            break;
        case '8':
            str[i] = PALABRA[8];
            break;
        case '9': 
            str[i] = PALABRA[9];
            break;
        
        default:
            break;
        }
    }

    
    printf("%s\n", str);
    return 0;
}