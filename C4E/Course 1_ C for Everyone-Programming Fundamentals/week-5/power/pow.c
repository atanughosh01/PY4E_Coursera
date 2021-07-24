// C program to calculate the power of an integer

#include <stdio.h>

int main()
{
    int exponent, expo;
    double base;
    long double result = 1.0;

    printf("\nEnter the number whose power is to be calculated");
    printf("\n(Result will be truncated upto 10th decimal place) : ");
    scanf("%lf", &base);

    printf("\nEnter the exponent of %lf to calculate : ", base);
    scanf("%d", &exponent);

    expo = exponent;

    if (exponent > 0)
    {
        while (exponent != 0)
        {
            result *= base;
            exponent--;
        }
        printf("\n%lf to the power %d is = %0.10Lf\n\n", base, expo, result);
    }
    else if (exponent < 0)
    {
        while (exponent != 0)
        {
            result *= (1.0 / base);
            exponent++;
        }
        printf("\n%lf to the power %d is = %0.10Lf\n\n", base, expo, result);
    }

    return 0;
}
