#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

int arr[9] = { 9,8,24,1,2,5,63,7,21 };
int num = 9;
int main(void) {
	int root = 0;
	int i,c, temp;
	//���� �ִ� �������� ��������
	for (i = 1; i < num; i++) {		
		c = i; //���� i��° ���� �� �θ� ã�ư�����?			

						//�� ���� �˰����� �� ��尡 �ڱ��� �θ� ��� ã�ư��鼭 
		do {				//�ڱⰡ �θ𺸴� ũ�� �θ�� �ڸ��� ��� ã�ư��� ����.
			root = (c - 1) / 2;	//c�� �θ���� (c-1)/2��° ��忡��.
			if (arr[root] < arr[c]) {//���� �θ𺸴� ũ�� ���� �������� �θ𿡿�.
				temp = arr[root];
				arr[root] = arr[c];
				arr[c] = temp;
			}
			c = root;//���� �θ��ڸ��� �Ծ��.
		} while (c != 0); //heapify�� ���������� ��� �ݺ�
	}
	//���� leaf���� root��带 �ٲ��ְ� �ٽ� �ִ��������� ����ϴ�.
	for (i = num - 1; i >= 0; i--) {
		temp = arr[0];
		arr[0] = arr[i];
		arr[i] = temp;

		root = 0;
		c = 1;

		do {
			c = 2 * root + 1;
			if (c < i - 1 && arr[c] < arr[c + 1]) {// c<i-1�� ������ ���� c��� ���� ��尡 ������ �����
				c++;// ������ ���� �̹� ������ �� �ֱ� ������ �ǵ��̸� �ȵǱ� �����̴�.
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
