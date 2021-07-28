//  Output of func(5) will be ?

#include <stdio.h>

int func(int);

int main()
{
    int num;
    printf("\nEnter Number : ");
    scanf("%d", &num);
    printf("\nValue of func(%d) = %d", num, func(num));
    printf("\n\n");

    return 0;
}

int func(int n)
{
    int x = 1, k;
    if (n == 1)
        return x;
    for (k = 1; k < n; ++k)
        x = x + func(k) * func(n - k);
    return x;
}
