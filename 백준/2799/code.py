info = list(map(int, input().split()))

M = info[0]
N = info[1]

apt = []

while len(apt) != 5*M+1:
    apt.append(input())

result = [0,0,0,0,0]

'''
1 2 3 4 - 6 7 8 9 - 11 12 13 14 ....
M = 1
N = 2
########### 0
#....#****# 1 - 1, 6
#....#****# 2 - 1, 6
#....#....# 3 - 1, 6
#....#....# 4 - 1, 6
########### 5 
'''


for i in range(M):
    idx_m = 1 + i * 5 # 1 6 11 ...
    info_m = [idx_m, idx_m + 1, idx_m + 2, idx_m + 3]
    for j in range(N):
        idx_n = 1 + j * 5 # 1 6 11 ...
        case = apt[info_m[0]][idx_n] + apt[info_m[1]][idx_n] + apt[info_m[2]][idx_n] + apt[info_m[3]][idx_n]
        if(case == '....'):
            result[0] += 1
        elif(case == '*...'):
            result[1] += 1
        elif(case == '**..'):
            result[2] += 1
        elif(case == '***.'):
            result[3] += 1
        else:
            result[4] += 1

print(result[0],result[1],result[2],result[3],result[4])        
