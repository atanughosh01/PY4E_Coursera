// C program to count whitespaces, digits, letters in english alphabet

#include <stdio.h>

int main(void)
{
    int blanks = 0, digits = 0, letters = 0, others = 0;
    int c;   // use for int value of character

    // while loop starts here
    while((c = getchar()) != EOF)
    {
        // if-elseif-else condition starts here
        if (c == ' ')
            ++blanks;
        else if (c >= 'O' && c <= '9')
            ++digits;
        else if (c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z')
            ++letters;
        else
            ++others;
    };

    // print the counts
    printf(" blanks = %d, digits = %d, letters = %d,", blanks, digits, letters);
    printf(" others = %d\n\n", others);

    return 0;
}
