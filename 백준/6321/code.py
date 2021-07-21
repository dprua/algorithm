for i in range(int(input())):
    name = input()
    print("String #{0}".format(i+1))
    for char in name:
        if ord(char) == 90:
            print("A",end='')
        else:
            num = ord(char)
            num+=1
            print(chr(num),end='')
    print('\n')