
#include<stdio.h>
#include"add.c"

//extern int count;

int main()
{
	int value;
	value = increment();
	//printf("%d\n", count);
	printf("%d\n", value);
	
	value = increment();
	//printf("%d\n", count);
	printf("%d\n", value);
	
	value = increment();
	//printf("%d\n", count);
	printf("%d\n", value);
	
	//count += 10;
	//value = count;
	
	//printf("%d\n", count);
	//printf("%d\n", value);
	
	return 0;
}
