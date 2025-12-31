class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []              #可以先建立一个空stack来累计放数：碰到符号就先不加了
        for i in tokens:
            if i in "+-*/" and nums:
                # 2. 统一在这里 Pop 两次（这就不用写 4 遍了）
                # 记住：先出来的是后面的那个数（b），后出来的是前面的数（a）
                end  = nums.pop()
                before_end = nums.pop()
                if i == "+" :
            
                    nums.append(before_end + end ) 
                elif i == "-"  :
                     
                    nums.append(before_end - end ) 
                elif i == "*"  :
                   
                    nums.append(before_end * end ) 
                elif i == "/"  :
             
                    nums.append(int(before_end / end) )  #❌题目要求 (向零截断)：比如−6/132应该得到 0 ；-6 // 132 会得到 -1。因为 Python 的 // 是往“更小的整数”
            else:    
                nums.append(int(i))
        return nums[0]

        #["2", "3", "4", "+"]
            #你担心的是：
            #前面已经有 3 个数了，那 + 到底该用哪几个？
            #剩下的状态是：
            #2   7
        """
            除非你人为规定：
            👉 只允许从末尾取
            一旦你规定了这一点——
            🌟它就已经是 Stack 了
        """

     
       
      