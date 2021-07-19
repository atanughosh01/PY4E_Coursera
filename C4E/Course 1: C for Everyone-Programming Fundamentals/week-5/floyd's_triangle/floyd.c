// C program to print floyd's triangle upto n rows

#include <stdio.h>

int main()
{
    int i, j, rows, n = 1;
    printf("\nEnter number of rows upto which triangle is to be prited : ");
    scanf("%d", &rows);

    for (i = 1; i <= rows; i++)
    {
        for (j = 1; j <= i; j++)
        {
            printf("%d ", n);
            n++;
        }
        printf("\n");
    }
    return 0;
}
