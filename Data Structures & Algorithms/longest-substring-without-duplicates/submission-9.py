class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #when to move left pointer：when a repeated letter is added
        #and move to where：        a unit right
        #(so that the substring started with L is void, a brand new subtring started )
        #record the length where the last unrepeated occur:+1

#        s = "zxyxyz"
#             L
#.              L
#                R

        window = set()
        L,R =0,0
        res = 0

        for R in range(len(s)):

           # if s[R] in window: 
           #the repeated letter is not neccessarily the left most one, so keep removing until the repeated one is gone in the substring
            while(s[R] in window):
                window.remove(s[L])
                L+=1
            #at this point the window is legitimate 
            window.add(s[R])
            res = max(res,R-L+1)
        return res


            


        