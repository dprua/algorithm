T = int(input())
result = 0.0
for i in range(T):
    a = list(map(str,input().split()))
    for info in a:
        if info == '@':
            result *= 3
        elif info == '%':
            result += 5
        elif info == '#':
            result -= 7
        else:
            result+=float(info)
    print("%.2f"% result)
    result = 0.0