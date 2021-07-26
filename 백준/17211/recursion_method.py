def find_o(info,types, floor, N):
    value_o = 0.0
    vlaue_x = 0.0
    if types == 0: #happy
        value_o = info[0]
        value_x = info[1]
    else:
        value_o = info[2]
        value_x = info[3]
    
    if floor == N:
        return value_o
    else:
        sum_1 = value_o * find_o(info,0,floor+1,N)
        sum_2 = value_x * find_o(info,1,floor+1,N)
        return sum_1+sum_2
def find_x(info,types, floor, N):
    value_o = 0.0
    vlaue_x = 0.0
    if types == 0: #happy
        value_o = info[0]
        value_x = info[1]
    else:
        value_o = info[2]
        value_x = info[3]
    
    if floor == N:
        return value_x
    else:
        sum_1 = value_o * find_x(info,0,floor+1,N)
        sum_2 = value_x * find_x(info,1,floor+1,N)
        return sum_1+sum_2
info_1 = list(map(int, input().split(" ")))
info_2 = list(map(float, input().split(" ")))

sum_happy = find_o(info_2,info_1[1],1,info_1[0])
sum_sad = find_x(info_2,info_1[1],1,info_1[0])
print(round(sum_happy * 1000))
print(round(sum_sad * 1000))
