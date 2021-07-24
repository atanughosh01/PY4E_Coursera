// C program to understand simple recursion

#include <stdio.h>

int func(int n)
{
    if (n == 1)
        return 1;
    else
        return 1 + func(n - 1);
}

int main()
{
    int n;
    printf("\nInput = ");
    scanf("%d", &n);
    printf("Output = %d\n\n", func(n));

    return 0;
}
