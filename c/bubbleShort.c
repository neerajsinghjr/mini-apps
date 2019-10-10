#include <stdio.h>
#include <ncurses.h>

void main() {
	int i, j, loop, search, swap, length=6;
	int array[] = {100, 50, 40, 90, 20, 1	0};

	// Given Array
	printf("Unordered Array: \n");
	for(i=0; i < length-1; i++){
		printf("%d \t", array[i]);
	}

	printf("\nWhat are your looking for: \n");
	scanf("%d \n", &search);

	// Shorted Bubble Array
	for(i=0; i < length-1 ; i++){
	  for(j=0; j < length-1; j++){
	  	if(array[j]>array[j+1]){
	  		if (array[i] == search){
	  			search = array[i];
	  		}
	  		swap = array[j];
	  		array[j] = array[j+1];
	  		array[j+1] = swap;
	  		loop++;
	  	}
	  }
	}

	printf("Ordered Array: \n");
	// Display Sorted Array
	for(i=0; i < length-1; i++){
		printf("%d \t", array[i]);
	}
	printf("\nSearch Result: %d", search);

	// noecho();

}