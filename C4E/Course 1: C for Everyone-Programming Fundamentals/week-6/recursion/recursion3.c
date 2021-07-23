// C program to calculate factorial of a function using recursion

#include <stdio.h>

unsigned long long fact(int n)
{
    if (n == 0)
        return 1;
    else
        return n * fact(n - 1);
}

int main()
{
    int num;
    do
    {
        printf("\nEnter Integer (Can't be < 0) : ");
        scanf("%d", &num);
    } while (num < 0);

    printf("Factorial of %d is = %llu\n\n", num, fact(num));

    return 0;
}
