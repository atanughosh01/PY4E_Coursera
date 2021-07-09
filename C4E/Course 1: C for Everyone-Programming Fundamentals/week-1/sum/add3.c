// 	Read In Three Floats And Print Sum

#include<stdio.h>

int main(void)
{
	float a, b, c, sum;

	// Read Entered Numbers 
	printf("Enter Three Numbers (Separated By Comma): ");
	scanf("%f, %f, %f", &a, &b, &c);
	printf("You Entered : a=%f, b=%f, c=%f", a, b, c);

	// Calculate Sum of Entered Numbers
	sum = a + b + c;
	printf("\nSum of %f, %f, %f is = %f", a, b, c, sum);

	return 0;
}
