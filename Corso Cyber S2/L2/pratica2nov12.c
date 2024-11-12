#include <stdio.h>

int main(){
    float numero1, numero2, media;

    printf("\nInserisci il primo numero: ");
    scanf("%d", &numero1);

    printf("\nInserisci il secondo numero: ");
    scanf("%d", &numero2);

    media =(numero1 + numero2)/ 2;

    printf("\nLa media aritmetica tra %d e %d è %.2d\n", numero1, numero2, media);

    return 0;
}