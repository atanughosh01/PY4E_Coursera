// C program to print all Strong Numbers within a given range

#include <stdio.h>

int isStrong(long long int);

int main()
{
    int num, l, r;
    printf("\nEnter 2 Integers You Want to Print Strong Numbers in b/w\n(Separated By Comma) : ");
    scanf("%d, %d", &l, &r);

    printf("\nSuch Numbers b/w %d and %d are : ", l, r);
    int count_num = 0;
    for (num = l; num <= r; num++)
    {
        if (isStrong(num) == 1)
        {
            count_num++;
            printf("%d ", num);
        }
    }
    printf("\n(Total %d Such Numbers)\n\n", count_num);
    return 0;
}

int isStrong(long long int num)
{
    int digit;
    long long int q, result = 0, fact = 1;

    q = num;
    while (q != 0)
    {
        digit = q % 10;
        while (digit != 0)
        {
            fact *= digit;
            digit--;
        }

        result += fact;
        fact = 1;
        q /= 10;
    }

    if (result == num)
        return 1;
    else
        return 0;
}
