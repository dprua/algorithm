def solution(grid, clockwise):
    answer = []
    
    # 1 / 3 2 1 / 5 4 3 2 1 -> n = 3
    # 1 / 3 2 1 / 5 4 3 2 1 / 7 6 5 4 3 2 1 -> n = 4
    
    for i in range(len(grid)):
        idx = 0
        for num in range(2*i+1,0,-1):
            print(grid[len(grid)-1][0])
            if(i==0):
                answer.append(grid[len(grid)-1][0])
            
    return answer

gird = ["1","234","56789"]
clockwise = True
a = solution(gird,clockwise)

print(a)