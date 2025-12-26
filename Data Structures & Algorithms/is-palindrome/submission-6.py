class Solution:
    def isPalindrome(self, s: str) -> bool:

       #using 2 pointers 方法
       #最明显的限制1：两指针相等吗：
       #用index作为指针，所以l< right
       #限制2:会有一些非字母：如同空格或者符号 如何跳跃过去？ #ord使用
                                        #跳跃多少
            
       #限制3：全部要一一致化大小写
        #注意，一定要实时更新l，r 
        l, r = 0 , len(s)-1

        while l<r:
            while l<r and not self.alpha_num(s[l]): #限制2:会有一些非字母：如同空格或者符号 如何跳跃过去？
                l +=1
            while l<r and not self.alpha_num(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): #限制1：两指针相等吗
                return False           #限制3：全部要一一致化大小写
            l += 1
            r -= 1

        return True
#

#如何判断是不是大写或者小写字母：##注意引用的时候要加self.alpha_num,和不能忘记填写argument
#做比较的时候 x本身也要加上ord
    def alpha_num(self,x):
        return (ord('a')<= ord(x) <= ord('z') or
                ord('A')<= ord(x) <= ord('Z')or
                ord('0') <= ord(x) <= ord('9'))
            


