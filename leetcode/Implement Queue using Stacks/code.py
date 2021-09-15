class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:      
        self.queue.insert(0,x)       
        
    def pop(self) -> int:
        length = len(self.queue)
        var = self.queue[-1]
        del self.queue[length-1]
        return var

    def peek(self) -> int:
        var = self.queue[-1]
        return var

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()