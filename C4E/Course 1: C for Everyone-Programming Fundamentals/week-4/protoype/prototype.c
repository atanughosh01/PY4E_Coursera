// C program to understand the eunction prototype

#include <stdio.h>

// declaring functions
double square(double);
double cube(double);

int main(void)
{
    // driver code goes here

    int how_many = 0, i, j;
    double interval = 0.0, div = 0.0, num = 0.0;

    printf("\nPrint squares and cubes from 1 to n where n is = ");
    scanf("%d", &how_many);

    printf("\nThe interval(>0 & <=1) of numbers you want to print squares and cubes for is = ");
    scanf("%lf", &interval);
    printf("\nInterval is = %lf", interval);

    if(interval > 0.0 && interval <= 1.0)        
        {
            div = (1.0 / interval);
            printf("\n\nNumber\t\tSquare\t\tCube\n");

            for (i = 1; i <= how_many; i++)
            {
                for (j = 0; j < div; j++)
                {
                    num = i + (j/div);
                    printf("\n%lf\t%lf\t%lf", num, square(num), cube(num));
                }
            }
        }
    else
    {
        printf("\nYou need to enter an interval which is >0 and <=1\n");
    }

    printf("\n\n");

    return 0;
}

// writing function definitions
double square(double x)
{
    return (x * x);
}

double cube(double x)
{
    return (x * x * x);
}
