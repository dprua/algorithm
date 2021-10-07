'''
-*- coding: utf-8 -*-

일반 테스트 케이스는 통과하였으나
시간복잡도가 O(n*200000) 이라 효율성 테스트는 통과하지 못했다.

삭제, 복구에 시간이 오래걸리는 문제가 있다.

개선 방법으로는 삽입,삭제가 빠른 linkedlist를 사용하여 구현하는 것이다.
'''

def solution(n, k, cmd):
    del_info = [] 
    state = ['O' for x in range(n)]
    idx = k   
    for cm in cmd:
        if cm == 'C':
            state[idx] = 'X'
            del_info.append(idx)
            temp = "".join(state)
            if 'O' not in state[idx:]: #마지막번째에 있는 걸 지웠다면
                idx = temp.rfind('O')
            else:
                idx = temp.find('O',idx)
        elif cm == 'Z':
            re = del_info.pop()
            state[re] = 'O'
        elif cm[0] == 'U':
            num = int(cm[2:])
            val = 0
            cur = idx - 1
            while num > 0:
                if state[cur] == 'O':
                    num -= 1
                val += 1
                cur -= 1
            idx -= val
        else:
            num = int(cm[2:])
            val = 0
            cur = idx + 1
            while num > 0:
                if state[cur] == 'O':
                    num -= 1
                val += 1
                cur += 1
            idx += val
            
    answer = "".join(state)
    return answer

