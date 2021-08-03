class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            find = 10
            _len = 1
            _num = num
            while True:
                if _num / find < 10:
                    break
                _num = _num / find
                _len += 1
            while num >= 10:
                _num = 0
                for i in range(_len+1):
                    _num = _num + num % 10
                    num = int(num / 10)
                _len = 1
                num = _num
                while True:
                    if _num / find < 10:
                        break
                    _num = _num / find
                    _len += 1
            return _num
            