class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        
        while n >= 4:
            n = n / 4
        
        if n == 1:
            return True
        else:
            return False
            