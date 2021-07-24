// C program to check wheather a number is Strong Number or not

#include <stdio.h>

int main()
{
    int digit;
    long long int q, num, result = 0, fact = 1;
    printf("\nEnter The Integer Number You Want to Check : ");
    scanf("%lld", &num);

    q = num;
    while (q != 0)
    {
        digit = q % 10;
        while (digit != 0)
        {
            fact *= digit;
            digit--;
        }

        result += fact;
        fact = 1;
        q /= 10;
    }

    if (result == num)
        printf("\nEntered Number %lld is a Strong Number.\n\n", num);
    else
        printf("\nEntered Number %lld is NOT a Strong Number.\n\n", num);

    return 0;
}
