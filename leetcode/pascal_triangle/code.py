class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if(numRows == 1):
            result = [[1]]
        elif(numRows == 2):
            result = [[1],[1,1]]
        else:
            result = [[1],[1,1]]
            for i in range(numRows-len(result)): # 5 - 2 = 3
                com = len(result)-1 # 2 - 1 = 1, com = 1, 2 ,3 ....
                result.insert(len(result),[1,1])
                for k in range(com):
                    idx = k+1
                    val = result[com][idx - 1] + result[com][idx]
                    result[len(result)-1].insert(idx, val)
        
        return result