// C program to check wheather a number is Armstrong Number or not

#include <stdio.h>

int main()
{
    int num, rem, result = 0, count = 0, mul = 1;
    printf("\nEnter The Integer Number You Want to Check : ");
    scanf("%d", &num);

    int q = num;
    while (q != 0)
    {
        q = q / 10;
        count++;
    }
    int cnt = count;
    q = num;

    while (q != 0)
    {
        rem = q % 10;
        while (cnt != 0)
        {
            mul *= rem;
            cnt--;
        }
        result += mul;
        q /= 10;
        mul = 1;
        cnt = count;
    }

    if (result == num)
        printf("\nEntered Number %d is an Armstrong Number.\n\n", num);
    else
        printf("\nEntered Number %d is NOT an Armstrong Number.\n\n", num);

    return 0;
}
