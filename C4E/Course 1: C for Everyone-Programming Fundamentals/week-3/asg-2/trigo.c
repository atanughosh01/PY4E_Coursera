// Write a program that can give the sine of a value between 0 and 1 (non inclusive). You will be graded based on whether
// the program can output a value in the correct range and whether your code is well-formatted and logically correct.

// 	# Review criteria

// Follow the style guidelines in the text, proper indention, one-line per statement, good choice of identifiers will
// figure prominently in grading.

// Peer grading standards will be based on documentation, good style, correctness, and elegance.

// 	# Peer Grading

// After submitting your work, you will get the opportunity to grade the work of three of your peers on a scale of 0-10.
// The grade is a sum of several categories and you should offer a brief remark on each category in
// the 'Overall evaluation/feedback' section. Your own work will also be assessed by your peers, from which we'll get
// your grade. Since you've worked hard on your submission and would like your peers to do a good job of assessing your
// work, please take your time and do a good job of assessing your peers' work in return.

// 	# Honor Code

// Please remember that you have agreed to the Honor Code, and your submission should be entirely yours.

// 	# Style Guidelines

// The following are very thoughtful guidelines recommended by Community TA Mike Roberts and endorsed by the rest of
// the staff. Keep in mind many IDE’s and programs such as gnu “indent” do some of this automatically.

// Everyone gets a few (2 for HW1, 5 for all others) style misstep freebies (typos happen) so do not markdown unless
// they are consistently inconsistent. Be lenient not rigid. Do comment on style issues you see when you grade them.

// Indenting - Must be consistent. Choice of indent size and whether tabs or spaces is used is up to the coder.
// One exception is that they may or may not like to indent the cases of a switch() and this is OK.

// Brace placement - Must be consistent across constructs, i.e. if they do opening brace on same line as a for()
// they should do the same style for all loops. Functions, classes, structs should use a consistent brace placement,
// but maybe different from the style used for executable statements.

// Comments - Files should have a file header comment (using either /* */ or // is fine). Functions should have a
// function comment (using either /* */ or // is fine). Other commenting is at the discretion of the coder.
// If you think they've done too little, too much, or have unclear comments do not dock them points, but do note
// that in the comment section when you grade them.

// Naming - Must be consistent in style, but there are many different named entities and people will be using
// different styles for different types of entities so be lenient unless they are clearly using two different
// styles for the same type of entity, i.e. member variables - mX and y aren't consistent,
// local variables - localVariable and my_counter aren't consistent.

// Among useful classics on programming elegantly is the “Taligent’s Guide To Designing Programs” Taligent Press 1994
// ISBN 0-201-40888-0. On page 30 they say:” Use comments” Comments aren’t a replacement for reading the code; source
// code should be as readable as possible. … If source code isn’t completely obvious, include a comment.”

// The Google C++ style guide says this:

// “Comments

// Though a pain to write, comments are absolutely vital to keeping our code readable. The following rules describe what
// you should comment and where. But remember: while comments are very important, the best code is self-documenting. Giving
// sensible names to types and variables is much better than using obscure names that you must then explain through comments.

// When writing your comments, write for your audience: the next contributor who will need to understand your code.
// Be generous — the next one may be you!”

/* ----------------------------------------------------------------------------------------------------------------------- */

// Write a C program that has a function that prints a table of values
// for sine and cosine between (0, 1). Upload your program as a text file.

// include required header files
#include <stdio.h>
#include <math.h> // needed for sin() and cos() functions

#define PI 3.14159 // define value of constant PI

// function to calculate sine and cosine values in the given range
void printValues(double gap)
{
    // declaring and initializing variables
    double degValue = 0.0, radValue = 0.0;

    for (degValue = 0.0; degValue <= 1.0; degValue += gap)
    {
        // convert the degree value to radian value
        radValue = degValue * (PI / 180.0);

        // calculate the sine and cosine functions
        double sinValue = sin(radValue);
        double cosValue = cos(radValue);

        // display the results
        printf("\tsin(%lf) = %lf", degValue, sinValue);
        printf("\tcos(%lf) = %lf\n", degValue, cosValue);
    }
}

// main method to implement functionalities
int main(void)
{
    double interval = 0.0;

    // prompting user for input of interval
    printf("\n  Enter the desired interval (>0 & <=1) : ");
    scanf("%lf", &interval);

    if (interval > 0.0 && interval <= 1.0)
        printValues(interval); // function is being called
    else
        printf("\n  Interval should be > 0 and <= 1\n\n");

    return 0;
}
