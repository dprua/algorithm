#include <stdio.h>



//int main() {
//
//	int i, j, temp;
//	int arr[10] = { 10,2,5,8,7,6,4,3,1,9 };
//
//	for (i = 1; i < 10; i++) {
//		j = i;
//		while (arr[j-1] > arr[j]) {  
//			temp = arr[j - 1];
//			arr[j - 1] = arr[j];
//			arr[j] = temp;
//			j--;
//		}
//	}
//
//	for (i = 0; i < 10; i++) {
//		printf("%d, ", arr[i]);
//	}
//}
//int main() {
//	int arr[10] = { 10,2,5,8,7,6,4,3,1,9 };
//	int i, j, temp;
//
//	for (i = 1; i < 10; i++) {
//		j = i;
//		while (arr[j] < arr[j-1]) {
//			temp = arr[j];
//			arr[j] = arr[j - 1];
//			arr[j - 1] = temp;
//			j--;
//		}
//	}
//	for (i = 0; i < 10; i++) {
//		printf("%d, ", arr[i]);
//	}
//}
