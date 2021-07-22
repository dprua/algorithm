class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        flag = True
        for idx in range(len(s)):
            if s[idx] == "A":
                absent_count+=1
                if absent_count >= 2:
                    return False
            elif s[idx] == "L":
                if (len(s) - idx) >= 3: #len(s)-1 - idx
                    if s[idx+1] == "L" and s[idx+2] == "L":
                        return False
            else:
                pass
        if flag:
            return True