class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x : len(x))

        if len(strs[0]) == 0:
            return ""
        else:
            result = ''

            for idx in range(len(strs[0])):
                flag = True
                for i in range(1,len(strs)):
                    if strs[0][idx] != strs[i][idx]:
                        flag = False

                if flag == True:
                    result += strs[0][idx]
                else:
                    return result
        return result