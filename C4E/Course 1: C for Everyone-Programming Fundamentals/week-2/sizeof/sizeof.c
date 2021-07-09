// To Print The Sizes of Allocated Memory for Basic Data Types in C

#include <stdio.h>

int main(void)
{
	printf("\n\t======== On My System ========\n\n");
	printf("\tSize of 'char' is %lu bytes\n", sizeof(char));
	printf("\tSize of 'int' is %lu bytes\n", sizeof(int));
	printf("\tSize of 'short' is %lu bytes\n", sizeof(short));
	printf("\tSize of 'long' is %lu bytes\n", sizeof(long));
	printf("\tSize of 'unsigned' is %lu bytes\n", sizeof(unsigned));
	printf("\tSize of 'long int' is %lu bytes\n", sizeof(long int));
	printf("\tSize of 'long long int' is %lu bytes\n", sizeof(long long int));
	printf("\tSize of 'float' is %lu bytes\n", sizeof(float));
	printf("\tSize of 'double' is %lu bytes\n", sizeof(double));
	printf("\tSize of 'long double' is %lu bytes\n", sizeof(long double));
	printf("\t------------------------------------\n\n");

	short short_a = 5;
	int normal_a = 67;
	unsigned unsigned_a = 67u;
	long long_a = 67l;

	printf("\tshort_a = %hd, divided by int 2 results in -> %d\n", short_a, short_a/2);
	printf("\tshort_a = %hd, divided by float 2 results in -> %lf\n", short_a, short_a/2.0);
	printf("\t67 as char is %c\n", normal_a);
	printf("\t------------------------------------\n\n");

	return 0;
}
