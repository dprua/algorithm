def number(num):
    try:
        a = int(num)
        return a
    except:
        return 0

n = int(input())
info = []

for i in range(n):
    a = input()
    len_a = len(a)
    count = 0
    for char in a:
        count += number(char)
    info.append((len_a,count,a))

info.sort()
for i in range(n):
    print(info[i][2])