class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        idx = 0
        g = sorted(g)
        s = sorted(s)

        for i in range(len(g)):
            if idx > len(s):
                break
            while idx < len(s):
                if(g[i] <= s[idx]):
                    count += 1
                    idx += 1
                    break
                else:
                    idx += 1
        return count

        