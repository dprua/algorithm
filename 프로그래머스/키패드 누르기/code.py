def solution(numbers, hand):
    answer = ''
    
    right = ['#','9','6','3']
    left = ['*','7','4','1']
    center = ['0','8','5','2']
    
    loc_r = 0
    info_r = '#'
    
    loc_l = 0
    info_l = '*'
    
    loc_c = 0
    
    for num in numbers:
        num = str(num)
        if num in right:
            loc_r = right.index(num)      
            answer+='R'
            info_r = num
        elif num in left:
            loc_l = left.index(num)
            answer+='L'
            info_l = num
        else:
            loc_c = center.index(num)
            
            dif_r = abs(loc_c-loc_r)
            dif_l = abs(loc_c-loc_l)
            
            if info_r in right:
                dif_r += 1
            if info_l in left:
                dif_l += 1
            
            if dif_r > dif_l:
                loc_l = center.index(num)
                answer+='L'
                info_l = num
            elif dif_l > dif_r:
                loc_r = center.index(num)
                answer+='R'
                info_r = num
            else:
                if hand == 'right':
                    loc_r = center.index(num)
                    answer+='R'
                    info_r = num
                else:
                    loc_l = center.index(num)
                    answer+='L'
                    info_l = num
            
    return answer



'''
1 2 3 [3]
4 5 6 [2]
7 8 9 [1]
* 0 # [0]
'''