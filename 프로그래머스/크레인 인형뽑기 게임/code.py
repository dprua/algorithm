def solution(board, moves):
    answer = 0
    [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    
    stk = []
    for idx in moves:
        idx = idx - 1
        i = 0
        val = 0
        for num in range(len(board)):
            if board[num][idx] != 0:
                val = board[num][idx]
                board[num][idx] = 0
                break
        if val == 0:
            continue
        else:
            if len(stk) != 0:
                top = stk.pop()
                if top == val:
                    answer+=2
                else:
                    stk.append(top)
                    stk.append(val)
            else:
                stk.append(val)
    return answer