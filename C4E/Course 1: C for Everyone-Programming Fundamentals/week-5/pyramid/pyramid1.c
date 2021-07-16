/*  Prints pyramid of stars
         *
        * *
       * * *
      * * * *
*/

#include <stdio.h>

int main()
{
    int i, j, n;
    printf("\nEnter the order of the square matrix : ");
    scanf("%d", &n);

    printf("\n====== Matrix ======\n\n");
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
            printf(" *");
        printf("\n");
    }

    printf("\n====== Pyramid ======\n\n");
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= 2 * n - 1; j++)
        {
            if (j >= n - (i - 1) && j <= n + (i - i))
                printf("* ");
            else
                printf(" ");
        }
        printf("\n");
    }

    return 0;
}
