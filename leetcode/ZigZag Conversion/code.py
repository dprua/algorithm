class Solution:
    def convert(self, s: str, numRows: int) -> str:       
        if numRows == 1:
            return s
        special = numRows - 2
        result = []
        idx = 0
        for i in range(numRows):
            result.append('')
        flag = True
        count = 0
        i = 0
        s_temp = special
        
        for char in s:
            if flag:
                result[i]+=char
                count += 1
                i += 1
                if special <= 0 and i >= numRows:
                    i = 0
                    count = 0
                if count == numRows and special > 0:
                    flag = False
                    count = 0
                    i = 0
            else:
                result[s_temp]+=char
                s_temp -= 1
                if s_temp == 0:
                    flag = True
                    s_temp = special

        ans = ''
        for text in result:
            ans += text

        return ans