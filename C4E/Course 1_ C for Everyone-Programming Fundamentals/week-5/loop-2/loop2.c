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
            break;
        case 1:
            i += 2;
            break;
        case 5:
            i += 5;
            break;
        default:
            i += 4;
            break;
        }
        printf("%d ", i);
    }

    return 0;
}
