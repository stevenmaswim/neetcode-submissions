class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: #in the case this is empty append the val
            cur_min = val
        else: 
            cur_min = min(val, self.stack[-1][1])
        self.stack.append((val, cur_min)) #this trick makes a stack of tuples
            

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
        
