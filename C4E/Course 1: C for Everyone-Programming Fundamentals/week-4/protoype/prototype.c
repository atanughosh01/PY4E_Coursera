// C program to understand the eunction prototype

#include <stdio.h>

double square(double);
double cube(double);

int main(void)
{
    int how_many = 0, i, j;
    double interval = 0.0;

    printf("\nI want square and cube for 1 to n where n is = ");
    scanf("%d", &how_many);

    

    return 0;
}

double square(double x)
{
    return (x * x);
}

double cube(double x)
{
    return (x * x * x);
}
