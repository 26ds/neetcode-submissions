class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        #needed to be pushed into 2 stack and record the minimum value at ech point
        
        self.stack.append(val)
        #value pushed into minstack is different :record the minimum value at ech point,the minimum is definitely on the top of the minstack
        val = min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
