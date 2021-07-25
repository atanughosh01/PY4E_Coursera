/* Example of Direct Recursion (Recursion in which the function calls itself indirectly)

A function (say func1) is called INDIRECT RECURSIVE if it calls another function (say func2)
and then the called function (func2) calls the caller function (func1) directly or indirectly

        func1()
        {
            // some code
            func2();
            // some code
        }

         func2()
        {
            // some code
            func1();
            // some code
        }
*/

// WAP to print numbers from 1 to N (user input) in such a way that when number is odd, add 1
// and when number is even, subtract 1

#include <stdio.h>

void odd(int);
void even(int);

int n = 1;

int main()
{
    int lim;
    printf("\nEnter Right Limit (Left Limit is 1) : ");
    scanf("%d", &lim);

    printf("\nSuch Numbers upto %d are : ", lim);
    odd(lim);
    printf("\n\n");

    return 0;
}

void odd(int lim)
{
    if (n <= lim)
    {
        printf("%d ", n + 1);
        n++;
        even(lim);
    }
    return;
}

void even(int lim)
{
    if (n <= lim)
    {
        printf("%d ", n - 1);
        n++;
        odd(lim);
    }
    return;
}
