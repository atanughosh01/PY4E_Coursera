// Convert Entered Farenheit Temparature to Celsius Temparature

#include<stdio.h>

int main(void)
{
	float farenheit, celsius;

	// Taking Farenheit Temparature as Input
	printf("\nEnter Temparature in Farenheit : ");
	scanf("%f", &farenheit);

	// Converting Farenheit Temparature to Celcius Temparature
	celsius = (farenheit - 32) * 5.0 / 9.0;		// conversion is done here
	printf("\n %f degrees of Farenheit = %f degrees of Celsius\n\n", farenheit, celsius);

	return 0;
}
