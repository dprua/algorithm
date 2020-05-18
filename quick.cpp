#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

void quick_sort(int* arr, int front, int rear);

int arr[10] = { 10,2,5,8,7,6,4,3,1,9 };

int main() {

	int i,front = 0,rear = 9;

	quick_sort(arr,front,rear);

	for (i = 0; i < 10; i++) {
		printf("%d, ", arr[i]);
	}
}

void quick_sort(int *arr,int front,int rear) {

	if (front >= rear) // 원소가 1개인 경우,1개미만인경우
		return ;

	int pivot = front;
	int start = front + 1;
	int end = rear;
	int temp;

	while (start <= end) { //엇갈릴때까지 반복
		while(arr[start] <= arr[pivot] && start <= end) {//pivot보다 큰값을 왼쪽에서부터 찾아감
			start++;	//>= 내림차순
		}
		while(arr[end] >= arr[pivot] && end >= start) {//pivot보타 작은값을 오른쪽에서부터 찾아감
			end--;	 //<= 내림차순
		}
		if (start > end) { // 엇갈렸으면
			temp = arr[pivot];
			arr[pivot] = arr[end];
			arr[end] = temp;
		}
		else {             // 엇갈리지 않았으면
			temp = arr[start];
			arr[start] = arr[end];
			arr[end] = temp;
		}
	}

	quick_sort(arr, front, end-1); //end위치는 정렬된 자리이므로 end를 기준으로 좌
	quick_sort(arr, end+1, rear);  //end위치는 정렬된 자리이므로 end를 기준으로 우
	
}
