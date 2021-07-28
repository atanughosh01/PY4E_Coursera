/* Example of TAIL_RECURSIVE Function

A recursive function is said to be non-tail-recursive if the recursive call is NOT the last
thing done by the function. After returning back there is something left to evaluate.

*/

#include <stdio.h>

void func(int);

int main()
{
    int num;
    printf("\nEnter the argument to be passed : ");
    scanf("%d", &num);

    printf("Output is : ");
    func(num);
    printf("\n\n");

    return 0;
}

void func(int n)
{
    if (n == 0)
        return;
    func(n - 1);
    printf("%d ", n);
}
