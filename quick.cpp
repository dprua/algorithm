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

	if (front >= rear) // ���Ұ� 1���� ���,1���̸��ΰ��
		return ;

	int pivot = front;
	int start = front + 1;
	int end = rear;
	int temp;

	while (start <= end) { //������������ �ݺ�
		while(arr[start] <= arr[pivot] && start <= end) {//pivot���� ū���� ���ʿ������� ã�ư�
			start++;	//>= ��������
		}
		while(arr[end] >= arr[pivot] && end >= start) {//pivot��Ÿ �������� �����ʿ������� ã�ư�
			end--;	 //<= ��������
		}
		if (start > end) { // ����������
			temp = arr[pivot];
			arr[pivot] = arr[end];
			arr[end] = temp;
		}
		else {             // �������� �ʾ�����
			temp = arr[start];
			arr[start] = arr[end];
			arr[end] = temp;
		}
	}

	quick_sort(arr, front, end-1); //end��ġ�� ���ĵ� �ڸ��̹Ƿ� end�� �������� ��
	quick_sort(arr, end+1, rear);  //end��ġ�� ���ĵ� �ڸ��̹Ƿ� end�� �������� ��
	
}
