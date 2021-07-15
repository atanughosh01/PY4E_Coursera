
#include <stdio.h>

int main()
{
	char a = 7;
	a ^= 5;
	printf("%d", printf("%d", a += 3));

	printf("\n--------------------------\n");

	int var, num;

	num = (var = 15, var + 35);
	printf("%d", num);

	printf("\n--------------------------\n");

	int p = 1;
	int q = 1;
	int r = ++p || q++;
	int s = q-- && --p;
	printf("%d %d %d %d\n\n", p, q, r, s);

	return 0;
}
