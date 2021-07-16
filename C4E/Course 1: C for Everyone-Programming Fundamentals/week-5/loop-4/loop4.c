// What will be the output of the following C program?

#include <stdio.h>

int main()
{
    int i = 0;
    for (printf(" one\n"); i < 3 && printf(" "); i++)
        printf("Hi!\n");
    printf("-----------------\n");

    unsigned int x = 500;
    int count = 0;
    while (x++ != 0)
        count++;
    printf("x = %d\n", x);
    printf("Count = %u\n", count+x);

    return 0;
}
