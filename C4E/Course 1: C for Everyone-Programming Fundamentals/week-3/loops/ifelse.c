// C program to understand the if-else flow control

#include <stdio.h>

int main() {

	int var = 0; // local variable for main
	printf("Before if-else block %d\n",var);

	// if-else block starts here
	if(1){
		int var = 100; // new local variable of if block
		printf("if block %d\n",var);
	}
	else{
		printf("Do nothing");
	}

	printf("After if block %d",var);

return 0;
}
