#include <stdio.h>

#define add(x, y) (x+y)

int main()
{
	printf("\nResult of expression = %d\n\n", 5 * add(4, 3));
	
	printf("Date : %s\n", __DATE__);
	printf("Time : %s\n\n", __TIME__);
	return 0;
}
