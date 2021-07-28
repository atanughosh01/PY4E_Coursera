/* Example of TAIL_RECURSIVE Function

A recursive function is said to be tail-recursive if the recursive call is the last
thing done by the function. There is no need to keep record of the previous state.

*/

#include<stdio.h>

void func(int);

int main()
{
	int num;
	printf("\nEnter the argument to be passed : ");
	scanf("%d", &num);

	printf("Output is : ");
	func(num);
	printf("\n\n");

	return 0;
}

void func(int n)
{
	if (n==0)
		return;
	else
		printf("%d ", n);
	return func(n-1);
}
