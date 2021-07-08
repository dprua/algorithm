from itertools import combinations 

def solution(nums):
    answer = 0
    
    i = len(nums)
    nums = sorted(nums)
    max_val = nums[i-1] + nums[i-2] + nums[i-3]
    aristo = []

    for i in range(max_val+1):
        aristo.append(i)
    for i in range(2,max_val+1):
        if(aristo[i] == 0):
            continue
        for j in range(i+i,max_val+1,i):
            if(j % i == 0):
                aristo[j] = 0
    
    com = list(combinations(nums,3))

    for i in com:
        if(aristo[sum(i)] != 0):
            answer+=1
            a = sum(i)

    return answer