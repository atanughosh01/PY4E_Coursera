// C program to understand the function call in a better way

#include <stdio.h>

int func(int);

int main()
{
    int val;
    val = func(435);
    // Value printed will be?
    printf("\nValue = %d\n\n", val);

    return 0;
}

int func(int num)
{
    int count = 0;
    while (num)
    {
        count++;
        num >> 1;
    }
    return count;
}
