class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        result_s = []
        result_t = []

        idx = 0
        for char in s:
            if char =='#':
                if idx == 0:
                    pass
                else:
                    idx -= 1
                    del result_s[idx]

            else:
                result_s.append(char)
                idx+=1

        idx = 0
        for char in t:
            if char =='#':
                if idx == 0:
                    pass
                else:
                    idx -= 1
                    del result_t[idx]

            else:
                result_t.append(char)
                idx+=1

        return result_t == result_s