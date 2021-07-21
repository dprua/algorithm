class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 0
        temp = ""
        if len(a)>len(b):
            temp += a
            if b in temp:
                return 1
            else :
                temp += a
                if b in temp:
                    return 2
                else:
                    return -1
        else:
            while len(temp) <= 4 * len(b):
                temp += a
                count += 1
                if temp.find(b) != -1:
                    return count
            return -1