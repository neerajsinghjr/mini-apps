#include <stdio.h>


void main() {
	
	int array[5] = {90, 10, 50, 45, 20};
	int i, j, forLoop, whileLoop, key;
	
	printf("Unordered Array \n");
	for(i=0; i<5; i++){
		printf("-) %d \n", array[i]);
	}

	// Insertion Sorting
	for(i=1; i<5; i++) {
		key = array[i];
		j = i-1;
		++forLoop;	// For Loop Count
		while(j>=0 && array[j]>key) {
			array[j+1]=array[j];
			j= j-1;
			++whileLoop;
		}	
		array[j+1] = key;
	}

	printf("Ordered Array \n");
	for(i=0; i<5; i++){
		printf("-) %d \n", array[i]);
	}

	// printf("Sizeof: %d\n", sizeof(array));
	printf("ForLoop Counts: %d \n", forLoop);
	printf("WhileLoop Counts: %d\n", whileLoop);

}


















	// int i, j, key;
	// for (i = 1; i < ; i++) 
	// {
	// 	j = i;
 // 		while (j > 0 && arr[j - 1] > arr[j]) 
 // 		{
 // 			key = arr[j];
 // 			arr[j] = arr[j - 1];
 // 			arr[j - 1] = key;
 // 			j--;
 // 		}
	// }

	// cout << "Sorted Array: ";
	// // print the sorted array
	// for(i=0;i < length )