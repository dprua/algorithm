#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

//1---------
//int main() {
//    int i, j, min, index=0, temp;
//    int arr[10] = { 1,2,5,8,7,6,4,3,10,9 };
//
//    for (i = 0; i < 10; i++) {
//        min = arr[i]; // 첫번째항을 최솟값으로 정함
//        for (j = i; j < 10; j++) {// 현 배열의 최솟값을 찾는 반복문
//            if (min >= arr[j]) { //만약에 현재 값이 최솟값보다 적으면
//                min = arr[j];    //최솟값을 현재 값으로 바꾸고
//                index = j;       //최솟값의 위치를 저장
//            }
//        }
//        temp = arr[index];       //맨 앞자리에 최솟값을 저장
//        arr[index] = arr[i];
//        arr[i] = temp;
//    }
//    for (i = 0; i < 10; i++) {
//        printf("%d, ", arr[i]);
//    }
//2-----------
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
