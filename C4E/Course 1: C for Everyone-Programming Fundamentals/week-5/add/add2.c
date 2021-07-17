// C Program to Add Two Numbers Without Using The Addition Operator

#include <stdio.h>

int main()
{
    int sum, carry, a, b;
    printf("\nEnter two numbers to add\n(Separated by comma) : ");
    scanf("%d, %d", &a, &b);

    while (b!=0)
    {
        sum = a ^ b;
        carry = (a & b) << 1;
        a = sum;
        b = carry;
    }
    printf("\nSum of two values is %d\n\n", sum);
    return 0;
}
