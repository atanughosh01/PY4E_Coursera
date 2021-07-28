// Output of func(3) will be ?

#include <stdio.h>

void func(int);

int main()
{
    int num;
    printf("\nEnter Number : ");
    scanf("%d", &num);
    printf("\nOutput of func(%d) : ", num);
    func(num);
    printf("\n\n");

    return 0;
}

void func(int n)
{
    static int d = 1;
    printf("%d ", n);
    printf("%d ", d);
    d++;
    if (n > 1)
        func(n - 1);
    printf("%d ", d);
}
