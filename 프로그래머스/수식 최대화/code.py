from itertools import permutations

def calc(operators,expression):
    
    for op in operators:
        for info in expression:
            if info in operators and info == op: # 현재 순위 연산자면
                while True:
                    try:
                        idx = expression.index(op)
                        idx =  expression.index(op)
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