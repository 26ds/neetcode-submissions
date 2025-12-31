class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #the method of stack
        stack = [] #是”字符“，‘字符’，。。。
        maxlen = 0
        for i in s:
            # 3. 核心修改：找到那个重复字的位置，把那个字和它前面的都切掉
            # 比如 ['a', 'b', 'c'] 来了 'b'
            # index是 1，我们需要保留 index+1 也就是 'c' 开始往后的
            if i in stack:
                maxlen = max(maxlen,len(stack))
                duplicate_index = stack.index(i)
                stack = stack[duplicate_index + 1 :]
            stack.append(i)
            maxlen = max(maxlen, len(stack))
            
        
        return maxlen