// C program to understand the calling by value of a function

int computeSum(int n)
{
    int sum = 0;
    for (; n > 0; n--)
    {
        sum += n;
    }
    return sum;
}

int calculateSum(int n)
{
    int sum = 0, i;
    for (i = 0; i <= n; i++)
    {
        sum += i;
    }
    return sum;
}


#include<stdio.h>

int main(void)
{
    printf("%d\n", computeSum(10));
    printf("%d\n", computeSum(10.5));

    printf("---------------------\n");

    printf("%d\n", calculateSum(10));
    printf("%d\n", calculateSum(10.5));

    return 0;
}
