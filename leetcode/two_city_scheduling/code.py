# -*- coding: utf-8 -*- 
'''
그리디 알고리즘 문제
cost(a) - cost(b)를 수행해서 A에 치우친? 애들을 먼저 뽑고
나머지 n명을 B로 보내면 된다.
- cost(a) - cost(b) 값으로 오름차순으로 정렬하기
'''
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        temp = []
        i = 0
        for cost in costs:
            var = cost[0] - cost[1]
            temp.append([var,i])
            i+=1

        temp = sorted(temp, key = lambda x:x[0])

        outputs = 0
        for a in range(len(costs)):
            if(a < len(costs)/2):
                outputs+=costs[temp[a][1]][0]
            else:
                outputs+=costs[temp[a][1]][1]
        
        return outputs

