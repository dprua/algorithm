class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                if(stack[len(stack)-1] == char):
                    stack.pop()
                else:
                    stack.append(char)
            #print(stack)
        string_s = ''.join(stack)
        return string_s