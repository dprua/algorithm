def solution(lottos, win_nums):
    answer = [6,6,5,4,3,2,1]
    col_num = 0
    zero_cnt = 0
    for num in lottos:
        if num in win_nums:
            col_num += 1
        if num == 0:
            zero_cnt += 1
    
    return answer[col_num+zero_cnt],answer[col_num]