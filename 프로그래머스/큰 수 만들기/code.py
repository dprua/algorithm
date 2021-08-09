"""
실패 1 - 그리디 알고리즘이길래 가장 작은 숫자를 지우면 된다고 생각했음.
def solution(number, k):
    answer = ''
    del_count = 0
    tg = 1
    len_info = len(number)
    while del_count < k:
        for idx in range(len(number)):
            if del_count >= k:
                break
            if int(number[idx]) == tg:
                del_count += 1
                number = number[0:idx] + number[idx+1:]
                if str(tg) not in number:
                    break
        tg+=1
    
    return number
"""
#올바른 접근법 - 큰 자리 수부터 작은 숫자들을 제거해 나가야함. 뒤에 있는 숫자가 앞에 있는 숫자보다 크다면 앞에 있는 숫자를 지워야하는 거임.
def solution(number, k):
    answer = ''
    del_count = 0
    result = []
    result.append(number[0])
    stk_ptr = len(result) - 1
    for idx in range(1,len(number)):
        while result and int(result[stk_ptr]) < int(number[idx]) and del_count < k:
            result.pop()
            stk_ptr -= 1
            del_count += 1
            if del_count >= k:
                break
        result.append(number[idx])
        stk_ptr += 1
    if del_count < k:
        for i in range(k-del_count):
            result.pop()
    answer = answer.join(result)
    return answer

print(solution('9999',2))