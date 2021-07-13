# -*- coding: utf-8 -*-

password = []
validate = []

vowel = ['a','e','i','o','u']

case1 = True #모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
case2 = True #모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
case3 = True #같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

while True:
    case2 = True
    s = input()
    if s == 'end':
        break

    password.append(s)
    case1 = False
    for c in s:
        if c in 'aeiou':
            case1 = True
            break

    if case1 == False:
        validate.append('F')
        continue
    count = -1
    char = 'V' # V(모음) or C(자음)
    #ptoui
    
    for c in s:
        if count == 3:
            case2 = False
            break
        if count == -1: #가장처음
            count = 1
            if c in vowel:
                char = 'V'
            else:
                char = 'C'
        elif c in vowel and char == 'V':
            count+=1
        elif c in vowel and char == 'C':
            count = 1
            char = 'V'
        elif char == 'C':
            count+=1
        else:
            char = 'C'
            count = 1
    if count == 3 or case2 == False:
        validate.append('F')
        continue
    
    
    case3 = True
    for i in range(1,len(s)):
        if s[i] == s[i-1] and s[i] not in 'eo': 
            case3 = False
            break

    mark = s[0]
    case3 = True
    for idx in range(1,len(s)):
        if s[idx] == mark:
            if s[idx] == 'e' or s[idx] =='o':
                continue
            case3 = False
            break
        else:
            mark = s[idx]

    if case3:
        validate.append('T')
    else:
        print("case3")
        validate.append('F')
    
        
for idx in range(len(password)):
    if validate[idx] == 'T':
        print('<'+password[idx]+'> is acceptable.')
    else:
        print('<'+password[idx]+'> is not acceptable.')
        