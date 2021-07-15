
#include <stdio.h>

int main()
{
	char x = 1, y = 2;					// x = 1(0000 0001), y = 2(0000 0010)

	if (x&y)							// 1 & 2 = 0(0000 0000)
		printf("\nResult of 1&2 is 1\n");
	else if(x&&y)						// 1 && 2 = TRUE && TRUE = TRUE = 1
		printf("\nResult of 1&&2 is 1\n");

	printf("\n--------------------------\n");

	char var = 4;						// 4 in binary = 0000 0100
	printf("\nvar = %d\n", var);
	printf("var << 1 = %d\n", var << 1);
	printf("var << 3 = %d\n", var << 3);
	printf("var >> 1 = %d\n", var >> 1);
	printf("var >> 3 = %d\n", var >> 3);

	printf("\n--------------------------\n");

	int a = 10, b = 5;
	printf("\nBefore XOR, a = %d and b = %d", a, b);
	a = a ^ b;
	b = a ^ b;
	a = a ^ b;
	printf("\nAfter XOR, a = %d and b = %d\n\n", a, b);

	return 0;
}
