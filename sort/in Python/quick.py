# -*- coding: utf-8 -*-

def quicksort(nums, front, rear):
    
    if(front >= rear):
        return

    pivot = front
    start = front+1
    end = rear

    while(start<=end): #엇갈리지 전까지
        while(nums[start]<=nums[pivot] and start <= end ):#피봇 값보다 큰 값의 index를 앞에서부터 찾기 = 작은 값의 index는 패스~
            start += 1
        while(nums[end]>=nums[pivot] and start <= end):#피봇 값보다 작은 값의 index를 끝에서부터 찾기 = 큰 값의 index는 패스~
            end -= 1
        
        if(end <= start):
            temp = nums[pivot]
            nums[pivot] = nums[end]
            nums[end] = temp
        else:
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp
    
    quicksort(nums,front,end-1)
    quicksort(nums,end+1,rear)

nums = [1,4,2,3,6,7,5,8,9,0]
print(nums)
quicksort(nums,0,9)
print(nums)
