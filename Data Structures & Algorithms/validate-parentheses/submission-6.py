class Solution:
    def isValid(self, s: str) -> bool:
        #后遇到的左括号，必须先被闭合
        #最后一个进入stack的必须先配对，成功后弹出：后进先出
        ##注意⚠️：stack不为空的时候才可以去配对，否则直接false：
            #边缘情况input：[ ) ] 此时stack由于没有左边括号为空⚠️，stack[-1]核对的时候会出错
        
        #stack=【】为空就是false
        #空容器 →  False    if not stack：就是stack空的时候 
                            # not stack = true 即 stack被赋予false 空的时候
        #非空容器 → True。   所以if stack就是不空的时候

        #🌟入栈（左半边）、出栈（被检查的一方是右半边）、最终检查。🌟

        stack = []
        hashmap = {'}':'{',')':'(',']':'['}
        for half in s: #先写右半边被检查的一半逻辑
            if half in hashmap: #（，人话：如果是右半括号，其实就是hashmap.keys())
                if stack and hashmap[half] == stack[-1]:
                    stack.pop() #pop 最后一个
                else:
                    return False
            else:
                stack.append(half)
        if not stack:
            return True
        else:
            return False

