// Sample progrm to understand the TAIL and NON_TAIL recursion

#include <stdio.h>

void func1(int);
void func2(int);

int main()
{
    int num1, num2;
	printf("\nEnter the argument to be passed : ");
	scanf("%d", &num1);
	num2 = num1;

	printf("\nOutput1 is : ");
	func1(num1);

	printf("\n\nOutput2 is : ");
	func2(num2);

	printf("\n\n");
    return 0;
}

void func1(int n)
{
    if(n==0)
        return;
        
    func1(n/2);
    printf("%d ", n%2);
}

void func2(int n)
{
    if(n<=0)
        return;
    printf("%d ", n);
    func2(2*n);
    printf("%d ", n);
}