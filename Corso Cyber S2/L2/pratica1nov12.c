#include <stdio.h>

int main()
{
    int primo;
    int secondo;
    int risultato;

    printf("\nInserisci il primo numero: ");
    scanf("%d", &primo);

    printf("\nInserisci il secondo numero: ");
    scanf("%d", &secondo);

    risultato = primo * secondo;

    printf("\n%d * %d\n = %d\n", primo, secondo, primo * secondo);

    return 0;
}