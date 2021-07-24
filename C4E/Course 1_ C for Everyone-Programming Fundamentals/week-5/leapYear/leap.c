// C program to check whether the entered year is leap year or not

#include <stdio.h>

int main()
{
    int year;
    printf("\nEnter the year : ");
    scanf("%d", &year);

    if (year % 100 == 0)
    {
        if (year % 400 == 0)
            printf("The year %d is a leap year\n\n", year);
        else
            printf("The year %d is NOT a leap year\n\n", year);
    }
    else if (year % 100 != 0)
    {
        if (year % 4 == 0)
            printf("The year %d is a leap year\n\n", year);
        else
            printf("The year %d is NOT a leap year\n\n", year);
    }
    return 0;
}
