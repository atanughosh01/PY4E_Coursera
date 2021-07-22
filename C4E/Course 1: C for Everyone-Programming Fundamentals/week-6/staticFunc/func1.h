static int func(int a, int b)
{
    static int c;
    c = a + b;
    return c;
}
