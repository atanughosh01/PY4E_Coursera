// C program to check wheather a number is perfect or not

#include <stdio.h>

int main()
{
    int i, num, sum = 0;
    printf("\nEnter a number to check if perfect or not : ");
    scanf("%d", &num);

    for (i = 1; i < num; i++)
    {
        if (num % i == 0)
            sum += i;
    }
    if (sum == num)
        printf("The number %d is perfect number\n\n", num);
    else
        printf("The number %d is NOT perfect number\n\n", num);
    return 0;
}
