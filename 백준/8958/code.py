# -*- coding: utf-8 -*-

score = 0
cnt = 1
n = int(input())
score_list = []

for i in range(n):
    status = input()
    score = 0
    cnt = 1
    for idx in range(len(status)):
        if(status[idx] == 'O'):
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)
