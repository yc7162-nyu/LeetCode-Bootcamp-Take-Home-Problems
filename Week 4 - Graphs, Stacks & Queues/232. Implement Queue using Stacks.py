class MyQueue:

    def __init__(self):
        self.mainS = []
        self.reverse = []

    def push(self, x: int) -> None:
        self.mainS.append(x)

    def pop(self) -> int:
        if len(self.reverse) != 0:
            return self.reverse.pop()

        while len(self.mainS) != 0:
            self.reverse.append(self.mainS.pop())
        
        return self.reverse.pop()

    def peek(self) -> int:
        if len(self.reverse) != 0:
            return self.reverse[-1]
        
        while len(self.mainS) != 0:
            self.reverse.append(self.mainS.pop())
        
        return self.reverse[-1]        

    def empty(self) -> bool:
        if len(self.mainS) == 0 and len(self.reverse) == 0:
            return True
        
        return False        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()