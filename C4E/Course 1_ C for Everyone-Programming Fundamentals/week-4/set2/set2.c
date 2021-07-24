
#include<stdio.h>

int main()
{
	int var = 0x43FF;

	printf("%x\n", var);	// hexadecimal
	printf("%X\n", var);	// hexadecimal
	printf("%d\n", var);	// decimal
	printf("%c\n\n", var);	// ascii value

	int a = 4, b = 3;
	printf("%d\n", a + ++b);
	printf("%d\n", a++ + b);
	printf("%d\n", a+++b);
	printf("%d\n", a++ + ++b);
	printf("%d\n", a+++ ++b);

	return 0;
}
