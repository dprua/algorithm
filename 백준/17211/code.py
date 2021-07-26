#DP

N, first = map(int,input().split(" "))
HH,HS,SH,SS = map(float, input().split(" "))

happy = [0 for i in range(N)]
bad = [0 for i in range(N)]

if first == 0:
    happy[0] = HH
    bad[0] = HS
else:
    happy[0] = SH
    bad[0] = SS

for i in range(1,N):
    happy[i] = happy[i-1] * HH + bad[i-1] * SH
    bad[i] = happy[i-1] * HS + bad[i-1] * SS

print(round(happy[N-1] * 1000))
print(round(bad[N-1] * 1000))