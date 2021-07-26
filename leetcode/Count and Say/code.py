class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        prev = self.countAndSay(n-1)

        count = 0
        idx = 0

        result = ''
        for char in prev:
            if(idx >= len(prev)):
                break
            cur_char = prev[idx]
            #print(cur_char,idx)        
            count+=1
            for i in range(idx+1,len(prev)):
                if prev[i] != cur_char:
                    break
                count+=1
            idx = idx + count
            result = result + str(count) + cur_char
            count = 0
        return result