// The program has a mistake. Redo the program in a text file and upload it
// by clicking "upload file" below. Your peers will then review your
// submission to see whether you have appropriately fixed the errors.

// The following code is supposed to produce the volume of a sphere as a
// double but is using ints. Fix this issue.

// 		#include<stdio.h>

// 		#define PI 3.14159

// 		int main(void)
// 		{ 
// 			int radius;
// 			printf(“Enter radius:”);
// 			scanf(“%d”, &radius);
// 			printf(“volume is : %d \n\n“, 4 *radius*radius*radius/3 );

// 			return 0;
// 		}

// Copy the code exactly as is, make your modifications to fix the program,
// then submit a text file of your code.


#include<stdio.h>

#define PI 3.14159

int main(void)
{ 
	// declare variables
	int radius;
	double volume;

	// take input
	printf("\nEnter Radius : ");
	scanf("%d", &radius);

	// display output
	volume = 4*PI*radius*radius*radius/3;	// calculate volume
	printf("\nEntered Radius(in int) : %d\n", radius);
	printf("Volume Is : %lf\n\n", volume);

	return 0;
}
