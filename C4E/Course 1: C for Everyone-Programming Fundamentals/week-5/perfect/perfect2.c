// C program to print all perfect numbers within given range

#include <stdio.h>

int isPerfect(int);

int main()
{
    int i, low, upp, count = 0;
    printf("\nEnter lower limit : ");
    scanf("%d", &low);

    printf("Enter upper limit (>1): ");
    scanf("%d", &upp);

    if (low <= 0)
        low = 1;

    if (upp <= 1)
        printf("\nUpper limit must be greater than 1\n\n");
    else if (low > upp)
        printf("\nUpper limit must be greater than Lower limit\n\n");
    else
    {
        printf("\nPerfect numbers in the given range are : ");
        for (i = low; i <= upp; i++)
        {
            if (isPerfect(i) == 1)
            {
                count++;
                printf("%d  ", i);
            }
        }
        printf("\n(Total %d such numbers)\n\n", count);
    }
}

int isPerfect(int n)
{
    int i, sum = 0;
    for (i = 1; i < n; i++)
    {
        if (n % i == 0)
            sum += i;
    }
    if (sum == n)
        return 1;
    else
        return 0;
}
