#include <stdio.h>


//int main() {
//	int i, j, temp;
//	int arr[10] = { 1,2,5,8,7,6,4,3,10,9 };
//
//	for (i = 0; i < 10; i++) {
//		for (j = 0; j < 9-i; j++) {
//			if (arr[j] > arr[j + 1]) {
//				temp = arr[j];
//				arr[j] = arr[j + 1];
//				arr[j + 1] = temp;
//			}
//		}
//	}
//	for (i = 0; i < 10; i++) {
//		printf("%d, ", arr[i]);
//	}
//}
//int main() {
//	int arr[10] = { 10,2,5,8,7,6,4,3,11,9 };
//	int i, j, temp, max;
//	for (i = 0; i < 10; i++) {		
//		for (j = 1; j < 10 - i; j++) {
//			if (arr[j] < arr[j-1]) {
//				temp = arr[j];
//				arr[j] = arr[j - 1];
//				arr[j - 1] = temp;
//			}
//		}
//	}
//	for (i = 0; i < 10; i++) {
//		printf("%d, ", arr[i]);
//	}
//}
