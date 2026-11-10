class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        #if i meet the operaters, i will start popping numbers and store the new result in the stack.
        for i in tokens:
            if i == "+":
                stack.append(stack.pop()+stack.pop())
            elif i == "-":
                #need second pop()ed to minus the first popped()
                #[b,a]
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == "*":
                stack.append(stack.pop()*stack.pop())
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                #special case of -3/2 =-1.5->-2
                #truncate to 0    int(-3/2) = -1
                stack.append(int(b/a))
            else:
                #"2" not 2 so use int
                stack.append(int(i))
        return stack[0]