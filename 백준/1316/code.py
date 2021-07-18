count = 0

for i in range(int(input())):
    word = input()
    pass_char = []
    current = ''
    info = list(set(word))#happya > h a p y
    flag = True
    for char in word:
        if char not in pass_char:
            pass_char.append(char)
            current = char
        else:
            if char == current:
                pass
            else:
                flag = False
                break
    if flag:
        count+=1

print(count)
        