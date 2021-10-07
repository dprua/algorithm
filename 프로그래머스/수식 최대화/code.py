'''
-*- coding: utf-8 -*-

내 코딩 실력이 너무 고전적인 스타일 이라는 것을 많이 느끼게 한 문제이다.
permutations 함수도 잘 몰라서 구글링을 통해 알아내서 활용할 수 있었다.
꾸역꾸역 풀기는 했는데 코드가 정말 마음에 들지 않는다.
나중에 다시 풀어볼 것이다. 
풀이과정은 현재 expression에 등장한 operator를 알아내서 이 operator로 만들 수 있는 조합을
permutations 함수를 통해 구한다.
본 문제는 모든 경우의 수를 탐색 및 비교해야하는 완전탐색 문제이다. 
따라서 구해진 조합의 순서대로 for문을 통해 전처리된 expression에서 우선순위에 맞게 연산을 수행한다.
'''

from itertools import permutations

def calc(operators,expression):
    
    for op in operators:
        for info in expression:
            if info in operators and info == op: # 현재 순위 연산자면
                while True:
                    try:
                        idx = expression.index(op)
                        num1 = expression.pop(idx-1)
                        operator = expression.pop(idx-1)
                        num2 = expression.pop(idx-1)
                        result = 0
                        if operator == '+':
                            result = int(num1) + int(num2)
                        elif operator == '-':
                            result = int(num1) - int(num2)
                        elif operator == '*':
                            result = int(num1) * int(num2)
                        
                        expression.insert(idx-1,result)
                    except:
                        break
                        
    return str(expression[0])

def prepro(operators,expression):
    tmp = ''
    exp = []
    for char in expression:
        if char.isdecimal(): #숫자라면
            tmp += char
        else: #연산자라면
            exp.append(tmp)
            tmp = ''
            exp.append(char)
    exp.append(tmp) # 숫자와 연산자 분리된 거 완성
    
    return calc(operators,exp)
    
def solution(expression):
    answer = 0
    operators = '+-*'
    op_ = [] # 0 - [+], 1 - [-], 2 - [*] 
    bogi = []
    
    for i in range(3):
        if operators[i] in expression:
            op_.append(operators[i])
    
    comb = permutations(op_,len(op_))

    for op_ in comb:       
        ans = prepro(op_,expression) # expression 전처리
        ans = abs(int(ans))
        bogi.append(ans)

    return max(bogi) 