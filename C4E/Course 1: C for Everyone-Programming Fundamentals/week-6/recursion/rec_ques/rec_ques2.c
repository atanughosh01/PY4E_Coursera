// What will be the output of the program when j = 50 and when j != 50

#include <stdio.h>

int func(int);

int main()
{
	int num;
	printf("\nEnter Number : ");
	scanf("%d", &num);

	func(num);
	return 0;
}

int func(int j)
{
    static int i = 50;
    int k;
    if(i == j)
    {
        printf("Something ");
        k = func(i);
        return 0;
    }
    else
        return 0;
}
