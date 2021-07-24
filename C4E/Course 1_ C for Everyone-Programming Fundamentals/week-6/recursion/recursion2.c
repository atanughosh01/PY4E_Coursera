// C program to understand simple recursion

#include <stdio.h>

int func(int n)
{
    if (n == 0)
        return 1;
    else if (n < 0)
        return func(n + 1);
    else
        return 7 + func(n - 2);
}

int main()
{
    int n;
    printf("\nInput = ");
    scanf("%d", &n);
    
    printf("Output = %d\n\n", func(n));

    return 0;
}
