T = int(input())

#k >= 1, n <= 14
#0층 1,2,3,4,5....,14
#1층 3호 = 0층 1~3호까지 사람들의 합 1+2+3 = 6
#2층 3호 = 1층 1~3호까지 사람들의 합
#2층 12호 = 1층 1~12호까지 사람들 합
for i in range(T):
    k = int(input())
    n = int(input())
    info = [x for x in range(1,n+1)]
    for floor in range(k):
        for room in range(1,n):
            info[room] += info[room-1]
        
    print(info[-1])
    