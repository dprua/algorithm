
n = int(input())
info = list(map(int, input().split(" ")))
result = []

for num in info:
    if not num in result:
        result.append(num)
result.sort()
for num in result:
    print(num,end = ' ')

'''
n = int(input())
info = sorted(list(set(map(int, input().split(" ")))))
print(info)
'''