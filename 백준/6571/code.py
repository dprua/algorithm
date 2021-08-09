
DP = []
DP.append(1)
DP.append(2)

for i in range(2,1001):
    val = DP[i-1] + DP[i-2]
    DP.append(val)

while True:
    a,b = map(int,input().split(' '))
    if a == 0 and b == 0:
        break
    else:
        count = 0
        for i in range(1001):
            if DP[i] >= a and DP[i] <= b:
                count+=1
        print(count)