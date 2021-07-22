s = input()
count = 0
for idx in range(len(s)):
    print(s[idx],end="")
    count+=1
    if count%10 == 0:
        print("")