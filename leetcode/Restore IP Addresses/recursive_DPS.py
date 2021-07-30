#recursive DFS

class Solution:
    def restoreIpAddresses(self, s: str):
        def _solve(cur, rem, depth=0):
            
            if depth == 4:
                #print(cur)
                if len(cur) == len(s)+3:
                    #print(cur)
                    #print(cur[:])
                    sol.append(cur[:])
                return
            
            for i in range(1, min(len(rem)+1, 4)): # 이 4는 IP가 총 4부분으로 분활되니 4를 넣어준 것 같은데? 결과를 보니 len(rem)+1 만해도 되나 4를 넣으면 속도가 개선된다.
                new = rem[0:i]
                #print(new,i)
                if 0 <= int(new) < 256 and not (int(new[0]) == 0 and len(new) > 1):
                    #print(new,i,depth)
                    #print(len(new))
                    if not cur: #가장 처음
                        #print(cur,depth)
                        _solve(new, rem[i:], depth+1)
                    else:
                        #print(cur,depth,i)
                        _solve(cur + '.' + new, rem[i:], depth+1)
        
        sol = []
        _solve([], s)
        return sol

a = Solution()

s = input()

result = a.restoreIpAddresses(s)

print(result)