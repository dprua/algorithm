class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = 0
        count_10 = 0
        for bill in bills:
            if bill == 5:
                count_5+=1
            elif bill == 10:
                count_10+=1
                count_5-=1
            else:
                count_5-=1
                if count_10 == 0:
                    count_5-=2
                else:
                    count_10-=1

            if count_5 < 0 or count_10 < 0:
                return False
        return True