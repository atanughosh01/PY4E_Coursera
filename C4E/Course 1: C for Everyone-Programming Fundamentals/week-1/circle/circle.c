// Calculate Area and Perimeter of a Circle of Given Radius

#include<stdio.h>

#define PI 3.14159

int main()
{
	double radius=0.0, perimeter=0.0, area=0.0;
	printf("Enter Radius (in metres) : ");
	scanf("%lf", &radius);

	perimeter = 2 * PI * radius;
	area = PI * radius * radius;

	printf("Radius = %lf m\nArea = %lf sq.m.\nPerimeter = %lf m\n", radius, area, perimeter);
}
