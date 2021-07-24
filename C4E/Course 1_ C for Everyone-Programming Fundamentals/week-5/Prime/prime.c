// C program to check whether a number is prime or not

#include <stdio.h>

int main()
{
    int num, i, flag = 1;   // flag is set to TRUE (at first number is assumed to be prime)

    printf("\nEnter a non-negetive integer to check if prime or not : ");
    scanf("%d", &num);

    if (num < 0)
    {
        printf("\nNegetive numbers are not allowed to be entered\n\n");
    }
    else if (num == 0 || num == 1)
    {
        printf("\n1 and 0 are neither prime nor composite\n\n");
    }
    else
    {
        for (i = 2; i <= num / 2; i++)
        {
            if (num % i == 0)
            {
                flag = 0;   // if divisible, flag is set to FALSE, i.e. number is non-prime
                break;
            }
        }
        if (flag == 1)
        {
            printf("\nEntered number %d is a prime number.\n\n", num);
        }
        else if (flag == 0)
        {
            printf("\nEntered number %d is a composite number.\n\n", num);
        }
    }

    return 0;
}
