/* What will be the output of the following C program?
    a) 5 10 15 20
    b) 7 12 17 22
    c) Compiler Error
    d) 16 21
*/

#include <stdio.h>

int main()
{
    int i;
    for (i = 0; i < 20; i++)
    {
        switch (i)
        {
        case 0:
            i += 5;
        case 1:
            i += 2;
        case 5:
            i += 5;
        default:
            i += 4;
        }
        printf("%d ", i);
    }

    return 0;
}
