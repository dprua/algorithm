#My version of recursive_DPS approach style code
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dps(cur, rem, depth=0):

            if depth == 4:
                if(len(cur) == len(s)+3):
                    sol.append(cur)
                return

            for i in range(1, min(len(rem)+1,4)):
                check = rem[0:i]
                if (int(check) >= 0 and int(check) <= 255) and know(check):
                    if not cur:
                        dps(check,rem[i:],depth+1)
                    else:
                        dps(cur+'.'+check,rem[i:],depth+1)

        def know(string):
            if int(string[0]) == 0:
                if len(string) > 1:
                    return False
                else:
                    return True
            else:
                return True
        
        sol = []
        dps('',s)
        return sol