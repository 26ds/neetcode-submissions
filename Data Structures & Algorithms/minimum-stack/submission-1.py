class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(val,self.minstack[-1] if self.minstack else val))
        #给每一个stack列表里面的值都在minstack中对应的位置设置一个最小值，如果minstack不为空的时候，
        #这样minstack的最后一个数就应该是最小的

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
         

    def getMin(self) -> int:
        return self.minstack[-1]
