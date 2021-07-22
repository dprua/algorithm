s = input()

for char in s:
    num = ord(char)
    if num <= 67:
        num += 23
    else:
        num-=3
    print(chr(num),end="")