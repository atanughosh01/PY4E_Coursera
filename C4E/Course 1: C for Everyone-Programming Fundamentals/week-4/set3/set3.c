
#include <stdio.h>

int main()
{
	int a = 5, b = 1;
	int incr;

	// if condition before '&&' is FALSE(0), condition after '&&' won't be executed
	// incr = (a < b) && b++;
	// incr = (a < b) && b--;
	// incr = (a > b) && b++;
	incr = (a > b) && b--;

	printf("\nincr = %d\n", incr);	// prints 0 if FALSE, 1 if TRUE
	printf("a = %d, b = %d\n\n", a, b);

	return 0;
}
