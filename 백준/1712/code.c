#include <stdio.h>
#define MAX 2100000000

int main(void) {

    int Fixed = 0, UnFixed = 0, Price = 0, Num = 0, Income = 0;

    scanf("%d %d %d", &Fixed, &UnFixed, &Price);
    if (UnFixed >= Price) {
        printf("%d", -1);
    }
    else {
        while (Fixed / (Price - UnFixed) >= Num) {//수입이 지출보다 적다면 반복,수입이 더많아질떄까지 반복
            ++Num;
        }
        printf("%d", Num);
    }
}