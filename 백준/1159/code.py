# -*- coding: utf-8 -*-

people_num = int(input())
people_list = []

for i in range(people_num):
    people_list.append(input())

alpha = {'a' : 0,'b' : 0,'c' : 0,'d' : 0,'e' : 0,'f' : 0,'g' : 0,'h' : 0,'i' : 0,'j' : 0,'k' : 0,'l' : 0,'m' : 0,'n' : 0,'o' : 0,'p' : 0,'q' : 0,'r' : 0,'s' : 0,'t' : 0,'u' : 0,'v' : 0,'w' : 0,'x' : 0,'y' : 0,'z' : 0, }

for name in people_list:
    first = name[0]
    alpha[first] += 1

result = ''

for char in alpha:
    if(alpha[char] >= 5):
        result+=char

if(result == ''):
    print("PREDAJA")
else:
    print(result)