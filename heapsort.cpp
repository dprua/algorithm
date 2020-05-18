#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

int arr[9] = { 9,8,24,1,2,5,63,7,21 };
int num = 9;
int main(void) {
	int root = 0;
	int i,c, temp;
	//먼저 최대 힙구조로 만들어야함
	for (i = 1; i < num; i++) {		
		c = i; //나는 i번째 노드야 내 부모를 찾아가볼까?			

						//이 분의 알고리즘은 한 노드가 자기의 부모를 계속 찾아가면서 
		do {				//자기가 부모보다 크면 부모랑 자리를 계속 찾아가는 거임.
			root = (c - 1) / 2;	//c의 부모노드는 (c-1)/2번째 노드에요.
			if (arr[root] < arr[c]) {//내가 부모보다 크면 나는 이제부터 부모에요.
				temp = arr[root];
				arr[root] = arr[c];
				arr[c] = temp;
			}
			c = root;//나는 부모자리에 왔어요.
		} while (c != 0); //heapify가 끝날때까지 계속 반복
	}
	//가장 leaf노드와 root노드를 바꿔주고 다시 최대힙구조를 만듭니다.
	for (i = num - 1; i >= 0; i--) {
		temp = arr[0];
		arr[0] = arr[i];
		arr[i] = temp;

		root = 0;
		c = 1;

		do {
			c = 2 * root + 1;
			if (c < i - 1 && arr[c] < arr[c + 1]) {// c<i-1인 이유는 만약 c노드 다음 노드가 마지막 노드라면
				c++;// 마지막 노드는 이미 정렬이 돼 있기 때문에 건들이면 안되기 때문이다.
			}
			if (c < i && arr[root] < arr[c]) {
				temp = arr[root];
				arr[root] = arr[c];
				arr[c] = temp;
			}
			root = c;
		} while (c < i);
	}

	for (i = 0; i < num; i++) {
		printf("%d ", arr[i]);
	}
}
