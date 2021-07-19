// C program to convert a binary number to its decimal equivalent

#include <stdio.h>

int main()
{
    int base = 1, rem;
    unsigned long long int decimal = 0, binary, num;
    printf("\nEnter the binary number that is to be converted to decimal : ");
    scanf("%llu", &binary);

    num = binary;
    while (binary != 0)
    {
        rem = binary % 10;
        decimal += rem * base;
        binary /= 10;
        base *= 2;
    }
    printf("The decimal equivalent of %llu is = %llu\n\n", num, decimal);
    return 0;
}
