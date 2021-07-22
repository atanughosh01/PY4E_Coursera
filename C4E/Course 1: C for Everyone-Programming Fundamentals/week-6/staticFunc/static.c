// C program to understand the implementation of static function

#include <stdio.h>
#include<stdlib.h>
#include "func1.h"

int func(int, int);

int main()
{
    int sum = func(3, 4);
    printf("%d\n", sum);

    return 0;
}
