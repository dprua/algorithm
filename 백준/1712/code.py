a = input().split()
e = int(a[2]) - int(a[1])
if int(a[2]) <= int(a[1]):
    d = -1
else:
    d = int(int(a[0]) / e) + 1

print(d)  