#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

//int main() {
//    int i, j, min, index=0, temp;
//    int arr[10] = { 1,2,5,8,7,6,4,3,10,9 };
//
//    for (i = 0; i < 10; i++) {
//        min = arr[i]; // ù��°���� �ּڰ����� ����
//        for (j = i; j < 10; j++) {// �� �迭�� �ּڰ��� ã�� �ݺ���
//            if (min >= arr[j]) { //���࿡ ���� ���� �ּڰ����� ������
//                min = arr[j];    //�ּڰ��� ���� ������ �ٲٰ�
//                index = j;       //�ּڰ��� ��ġ�� ����
//            }
//        }
//        temp = arr[index];       //�� ���ڸ��� �ּڰ��� ����
//        arr[index] = arr[i];
//        arr[i] = temp;
//    }
//    for (i = 0; i < 10; i++) {
//        printf("%d, ", arr[i]);
//    }
//int main() {
//	int arr[10] = { 10,2,5,8,7,6,4,3,1,9 };
//	int i, j, temp, min, index=0;
//	for (i = 0; i < 10; i++) {
//		min = arr[i];
//		index = i;
//		for (j = i+1; j < 10; j++) {
//			if (arr[j] < min) {
//				min = arr[j];
//				index = j;
//			}
//		}
//		temp = arr[index];
//		arr[index] = arr[i];
//		arr[i] = temp;
//	}
//	for (i = 0; i < 10; i++) {
//		printf("%d, ", arr[i]);
//    }
//}
