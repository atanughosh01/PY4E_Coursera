// C program to understand the execution of ternery operators

#include<stdio.h>

int main(void)
{
	int speed;
	printf("\nEnter the speed as an integer : ");
	scanf("%d", &speed);

	// ternery operator goes here
	speed = (speed <= 65)? (65) : (speed <= 70)? (70) : (90);

	// switch statement goes here
	switch(speed)
	{
		case 65:
			printf("\nNo Speeding Ticket\n\n");
			break;
		case 70:
			printf("\nNormal Speeding Ticket\n\n");
			break;
		case 90:
			printf("\nExpensive Speeding Ticket\n\n");
			break;
		default:
			printf("\nIncorrect Speeding Ticket\n\n");
	}

	return 0;
}
