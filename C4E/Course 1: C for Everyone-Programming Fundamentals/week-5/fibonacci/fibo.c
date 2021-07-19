// C program to print the fibonacci series using loops

#include<stdio.h>

int main()
{
    int n, i;
    unsigned long long int result, a = 0, b = 1;
    printf("\nEnter number of terms to be printed : ");
    scanf("%d", &n);
    printf("\nFirst %d Fibonacci numbers are : ", n);
    
    for (i = 0; i < n; i++)
    {
        printf("%llu ", a);
        result = a + b;
        a = b;
        b = result;
    }
    printf("\n\n");
    return 0;
}
