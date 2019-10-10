#include <stdio.h>

void main() {
	int array[100], i, j, size, temp, min;

	printf("How much element you want: ");
	scanf("%d \n", &size);
	
	// Un-Ordered Array
	printf("Now Enter Value....\n");
	for(i=0; i < size-1; i++) {
		scanf("%d \n", &array[i]);
	}

	for (i=0; i < size; i++) {
		min = i;	// assuming the minimum value is at first index;
		for (j=i+1; j < size-1; j++) {
			if(array[min] > array[j]) {
				temp = array[min];
				array[min] = array[j];
				array[j] = temp;
			}
		}
	}

	// Ordered Array
	for(i=0; i < size-1; i++) {
		scanf("%d \n", &array[i]);
	}

}
