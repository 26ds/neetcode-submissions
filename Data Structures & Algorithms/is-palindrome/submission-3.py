class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1:先把特殊符号全部都去除掉/小写化，变成纯小写连接在一起的字母
        neeted =""
        for i in s:
            if i.isalnum():#检查是不是字母或数字，否则不会加入最后的倒叙""
                neeted +=i.lower() #是字母或数字，全部转换为小写！！别忘了
        return neeted == neeted[::-1]
        
        