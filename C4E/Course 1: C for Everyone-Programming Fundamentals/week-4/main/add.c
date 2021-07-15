
// static int count;

int increment()
{
	// int count = 0;
	static int count;
	count += 1;
	return count;
}
