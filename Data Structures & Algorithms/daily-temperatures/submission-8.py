class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        # add the temperature into stack and compare it to the last one，keep popping until it is not smaller thant he last one.
        # adding the difference of index of popped one and the current one into the res array
        # if the stack is empty or not smaller： adding the [temp,index] into stack

        for i, t in enumerate(temperatures):
            #进入 while，执行 stack.pop()，此时栈变成空的 [] 了。回到 while 头部进行下一轮判断，代码依然会去执行 stack[-1][0] < t，对空列表取 [-1] 就直接触发了 IndexError: list index out of range。
            while stack and stack[-1][0]<t:
                found = stack.pop() #[temp, index]
                res[found[1]] = i-found[1]#找到的i - stack最后一个的index
                
                    
            stack.append([t,i])
        return res
             
        