storage = []
chk = 0
for i in range(10):
    num = int(input())
    var = num % 42
    if not var in storage:
        storage.append(var)
        chk += 1
print(chk)