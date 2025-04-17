// Eric Cerna L. 22127660-4
#include <stdio.h>
#define VEL 1.6

int main() {
    float km_h, m_seg; 
    km_h = VEL * 60;
    m_seg = (VEL * 1000) / 60;

    printf("La velocidad de %.2f km/min, equivale a %.2f km/h y %.2f m/seg.\n", VEL, km_h, m_seg);
}