class MinStack:
    
    def __init__(self):
        self.stack = []
        self.t = -1
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.t+=1
        return

    def pop(self) -> None:
        self.t-=1
        self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[self.t]

    def getMin(self) -> int:
        return min(self.stack)
