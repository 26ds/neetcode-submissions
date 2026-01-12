class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s)-1

        while l<r:
            #首先处理不是字母或者数字的情况
            while l<r and not self.alpha_num(s[l]):
                l+=1
            while l <r and not self.alpha_num(s[r]):
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True



    def alpha_num(self,x):
        return (ord('a')<= ord(x) <= ord('z') or
                ord('A')<= ord(x) <= ord('Z')or
                ord('0') <= ord(x) <= ord('9'))
            
