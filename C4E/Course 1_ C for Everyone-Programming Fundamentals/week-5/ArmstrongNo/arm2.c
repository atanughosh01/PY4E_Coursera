// C program to print all Armstrong Numbers within a given range

#include <stdio.h>

int isArmstrong(int);

int main()
{
    int num, l, r;
    printf("\nEnter 2 Integers You Want to Print Armstrong Numbers in b/w\n(Separated By Comma) : ");
    scanf("%d, %d", &l, &r);

    printf("\nSuch Numbers b/w %d and %d are : ", l, r);

    int count_num = 0;
    for (num = l; num <= r; num++)
    {
        if (isArmstrong(num) == 1)
        {
            count_num++;
            printf("%d ", num);
        }
    }
    printf("\n(Total %d Such Numbers)\n\n", count_num);
    return 0;
}

int isArmstrong(int n)
{
    int rem, count = 0, mul = 1;
    long long int q, result = 0;

    q = n;
    while (q != 0)
    {
        q = q / 10;
        count++;
    }
    int cnt = count;
    q = n;

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

    if (n == result)
        return 1;
    else
        return 0;
}
