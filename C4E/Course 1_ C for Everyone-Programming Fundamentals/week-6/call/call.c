// c program on function call

#include <stdio.h>

int func();

int main()
{
    for (func(); func(); func())
        printf("%d ", func());

    return 0;
}

int func()
{
    static int num = 16;
    return num--;
}
