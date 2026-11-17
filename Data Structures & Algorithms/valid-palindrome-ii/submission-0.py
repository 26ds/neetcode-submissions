class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        count = 0
        #⚠️重点思路，当目前两个指针的大小不一样时：如果移去任意一个然后剩下的倒数是本身，
        #如果这两个指针删除后都check过revers过不相同，（由于最多移掉一个，那证明移除掉一个后还需要再移除>=1个）return False
        while l<r:
            if s[l] != s[r]:
                #去除左边or去除右边,右边是exclusive的
                if s[l+1:r+1] == s[l+1:r+1][::-1] or s[l :r] == s[l :r ][::-1]:
                    return True
                else:
                    return False
            r -=1
            l+=1
        return True 
        #一个都不需要去除的
                    



        