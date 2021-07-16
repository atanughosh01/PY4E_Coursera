// Check If The Number Is Palindrome Number

#include <stdio.h>

int main()
{
    int n, result = 0, q, rem;
    printf("\nPlease Enter The Number : ");
    scanf("%d", &n);

    q = n;
    while (q != 0)
    {
        rem = q % 10;
        result = result * 10 + rem;
        q /= 10;
    }

    if (result == n)
        printf("Entered Number is a Palindrome\n\n");
    else
        printf("Entered Number is NOT a Palindrome\n\n");

    return 0;
}
