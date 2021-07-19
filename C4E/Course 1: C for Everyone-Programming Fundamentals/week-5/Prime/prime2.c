// C program to print prime numbers within given range

#include <stdio.h>

int main()
{
    int i, j, low, upp, flag, count = 0;

    // Input upper and lower limit to print prime
    printf("\nEnter lower limit : ");
    scanf("%d", &low);

    printf("Enter upper limit : ");
    scanf("%d", &upp);

    if (low < upp && upp >= 3)
    {
        printf("\nAll prime numbers b/w %d and %d are : ", low, upp);

        // make sure that lowerlimit does not go below 2
        // since 2 is first prime number
        if (low < 2)
            low = 2;

        // find all Prime numbers between lowerlimit and upperlimit
        for (i = low; i <= upp; i++)
        {
            flag = 1; // assume that the current number is Prime

            // check if the current number i is prime or not
            for (j = 2; j <= i / 2; j++)
            {
                if (i % j == 0)
                {
                    flag = 0;   // not prime if divisible by a number other than 1 and itself
                    count++;    // increment the count by 1
                    break;
                }
            }
            if (flag == 1) // if prime, print it
            {
                printf("%d ", i);
            }
        }
        printf("\n\n(Total %d prime numbers between %d and %d)\n\n", count, low, upp);
    }
    else if (low > upp)
        printf("\nUpper Limit must be a greater integer than the Lower Limit\n\n");
    else
        printf("\nUpper Limit must be greater than or equal to 3\n\n");

    return 0;
}
