#include <stdio.h>

//Union-Find(합집합 찾기 알고리즘)
//모든 데이터의 크기 범위를 메모리 상에 표현할 수만 있다면 O(N)이라는 압도적인 속도로 정렬을 수행할 수 있다.

int getParent(int* parent, int x){  //부모의 값을 return해주는 함수
	if (parent[x] == x) return x;	//자식값과 부모값이 같으면 해당 값을 return
	return parent[x] = getParent(parent, parent[x]);  //같지 않으면 그 부모값을 가지고 그 부모의 부모값을 찾으러감.
}

void unionParent(int* parent, int a, int b) {	//두 노드를 연결해주는 함수
	a = getParent(parent, a);	//a의 부모값을 가져와라
	b = getParent(parent, b);	//b의 부모값을 가져와라
	if (a < b)			//a의 부모값이 더 적으면
		parent[b] = a;  //b의 부모값을 a로
	else                //반대
		parent[a] = b;
}

int compareParent(int* parent, int a, int b) {	//두 노드의 부모의 값이 같으면 1 다르면 0 반환
	a = getParent(parent, a);	//a의 부모값을 가져와라
	b = getParent(parent, b);	//b의 부모값을 가져와라
	if (a == b)
		return 1;
	else
		return 0;
}
int main() {
	int parent[11];
	int i;

	for (i = 1; i <= 10; i++) {
		parent[i] = i;
	}

	unionParent(parent, 1, 2);
	unionParent(parent, 2, 3);
	unionParent(parent, 3, 4);
	unionParent(parent, 5, 6);
	unionParent(parent, 6, 7);
	unionParent(parent, 7, 8);
	
	printf("1과 2는 연결되어 있나요? : %d\n", compareParent(parent, 1, 2));
	printf("1과 5는 연결되어 있나요? : %d\n", compareParent(parent, 1, 5));

	unionParent(parent, 4, 5);

	printf("1과 5는 연결되어 있나요? : %d\n", compareParent(parent, 1, 5));
}
