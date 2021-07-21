// C program to understand how a function is called by refrerence

#include <stdio.h>

int func(int*, int*);

int main()
{
    int x = 10, y = 20;
    func(&x, &y);

    printf("\nx = %d, y = %d\n\n", x, y);

    return 0;
}

int func(int *ptr1, int *ptr2)
{
    *ptr1 = 20;
    *ptr2 = 10;
}
