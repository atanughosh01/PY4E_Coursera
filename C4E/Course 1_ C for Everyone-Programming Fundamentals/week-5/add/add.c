// C Program to Add Two Numbers Without Using The Addition Operator

#include <stdio.h>

int main()
{
    int x, y;
    printf("\nEnter two numbers to add\n(Separated by comma) : ");
    scanf("%d, %d", &x, &y);

    if (y > 0)
    {
        while (y != 0)
        {
            x++;
            y--;
        }
    }
    else if (y < 0)
    {
        while (y != 0)
        {
            x--;
            y++;
        }
    }
    printf("\nSum of two values is %d\n\n", x);
    return 0;
}
