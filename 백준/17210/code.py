num = int(input())
way = int(input())
if num > 5:
    print("Love is open door")
else:
    if way == 0:
        for i in range(num-1):
            if i % 2 == 0:
                print(1)
            else:
                print(0)
    else:
        for i in range(num-1):
            if i % 2 == 0:
                print(0)
            else:
                print(1)