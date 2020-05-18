#include <stdio.h>

//모든 데이터의 크기 범위를 메모리 상에 표현할 수만 있다면 O(N)이라는 압도적인 속도로 정렬을 수행할 수 있다.

int main() {
	int count[5];
	int arr[30] = { 1,3,2,4,1,2,1,3,4,1,
				   2,3,1,1,4,1,2,3,1,1,
				   3,2,4,1,1,2,3,1,4,2 };
	int i,j, temp;

	for (i = 0; i < 5; i++) {
		count[i] = 0;
	}

	for (i = 0; i < 30; i++) {
		count[arr[i] - 1]++;
	}

	for (i = 0; i < 5; i++) {
		printf("%d ", count[i]);
	}
	printf("\n");	
	for (i = 0; i < 5; i++) {
		temp = i + 1;
		for (j = 0; j < count[i]; j++) {
			printf("%d", temp);
		}
	}
}
