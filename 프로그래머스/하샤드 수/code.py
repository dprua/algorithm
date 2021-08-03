def solution(x):
    answer = True
    
    if x < 10:
        return answer
    else:
        find = 10
        _len = 1
        _x = x
        num = 0
        while True:
            if _x / find < 10:
                break
            _x = _x / find
            _len+=1
        _x = x
        for i in range(_len+1):
            num += _x % 10
            _x = int(_x / 10)
        if x % num == 0:
            return True
        else:
            return False