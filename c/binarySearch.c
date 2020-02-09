#include <stdio.h>

void main() {
	int array[5] = {90, 10, 50, 45, 20};
	int i, j, key, low, high, mid, count;

	printf("Enter Key: ");
	scanf("%d \n", &key);t

	low = 0;
	high = 5;

	while(low<high){
		mid = (low+high)/2;
		count++;
		if(array[low] == key || array[high] == key){
			printf("Success");
			break;
		}else if(array[mid] == key){
			printf("Success");
			break;
		}else{
			if(array[mid] < key){
				low=mid;
			}else if(array[mid] > key){
				high=mid;
			}
			else{
				printf("Fail!");
			}
		}
	}

	printf("Count %d", count);
}