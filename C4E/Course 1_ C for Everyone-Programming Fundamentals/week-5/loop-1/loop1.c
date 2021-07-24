// How many times will "Hello, World" be printed in the program?

#include <stdio.h>

int main()
{
    int i = 1024;
    int count = 0;

    for (; i; i >>= 1) // Note that i >>= 1 is eqv to i = i >> 1 , i.e. i = i/2
    {
        printf("Hello, World\n");
        count++;
    }
    printf("\nHello, World is printed %d times\n\n", count);

        return 0;
}
