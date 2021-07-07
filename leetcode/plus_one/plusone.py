class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur = 1
        flag = True
        length = len(digits)
        while flag:
            if(cur > len(digits)):
                digits.insert(0,1)
                flag = False
            else:
                digits[length-cur] += 1
                if(digits[length-cur] >= 10):
                    digits[length-cur] = 0
                    cur += 1
                else:
                    flag = False
        return digits