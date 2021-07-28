/*	Determine how many number of times star ("*") will be printed on the screen

void func1(int n)
{
	int i = 0;
	if(n > 1)
		func1(n - 1);
	for (int i = 0; i < n; ++i)
		printf(" * ");
}

a) n 	b) n(n + 1)/2 	c) n*n 	  d) NONE	*/

#include <stdio.h>

void func1(int);

int main()
{
	int num;
	printf("\nEnter Number : ");
	scanf("%d", &num);

	func1(num);
	return 0;
}

void func1(int n)
{
	int i = 0;
	if(n > 1)
		func1(n - 1);
	for (int i = 0; i < n; ++i)
			printf(" * ");
}
