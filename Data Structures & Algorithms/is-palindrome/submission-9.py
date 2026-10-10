class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2 pointers  always keep looping when left pointers is on the left side of the right pointers)
        l,r = 0, len(s)-1
        while l<r:
            #make sure it is letter or num , skip those who is not
            while l<r and not self.isalphaNum(s[l]):
                l+=1
            while l<r and not self.isalphaNum(s[r]):
                r-=1
            
            #if not equal, opt out with false
            # if eqaul ,keep the l,r pointers going
            if s[l].lower() != s[r].lower(): #🌟，一律转换成为 lower 来比较
                return False
             #keep the pointers moving toward the center of the word
            l+=1
            r-=1
             # ready for the next turn
        return True
        

    def isalphaNum(self,c):
            return(ord("A")<=ord(c)<=ord("Z")or
            ord("a")<=ord(c)<=ord("z")or
            ord("0")<=ord(c)<=ord("9"))    
