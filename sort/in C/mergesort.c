#include <stdio.h>


void merge(int* arr, int n, int middle, int m);
void merge_sort(int* arr, int n, int m);

int number = 8;
int sorted[8];

int main() {
	int i;
	int arr[8] = { 4,2,3,1,5,7,6,8 };
	merge_sort(arr, 0, number-1);

	for (i = 0; i < number; i++) {
		printf("%d ", arr[i]);
	}
}

void merge(int *arr,int n,int middle,int m) {
	int i = n;
	int j = middle + 1;
	int k = n;
	int t;

	while (i <= middle && j <= m) {
		if (arr[i] <= arr[j]) {
			sorted[k] = arr[i];
			i++;
		}
		//else문 대신에 if문으로 짜면 안되는 이유
		else {
			sorted[k] = arr[j];
			j++;			
		}
		k++;
	}
	if (i > middle) {
		for (t = j; t <= m; t++) {
			sorted[k] = arr[t];
			k++;
		}
	}
	//else문 대신에 if문으로 짜면 안되는 이유
	else {
		for (t = i; t <= middle; t++) {
			sorted[k] = arr[t];
			k++;
		}
	}
	for (t = n; t <= m; t++) {
		arr[t] = sorted[t];
	}
}
void merge_sort(int* arr,int n,int m) {
	if (n < m) {
		int middle = (n + m) / 2;
		merge_sort(arr, n, middle);
		merge_sort(arr, middle + 1, m);
		merge(arr, n, middle,m);
	}
	return ;
}
