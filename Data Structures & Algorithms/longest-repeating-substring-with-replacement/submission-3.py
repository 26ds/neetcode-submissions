class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #不用default dict
        #需要获得最长的窗口 连续没有打断
        #扩大窗口通过R
        #1:如何保证窗口合法？：
        #2:什么是合法窗口？： 最大的
        #3:while 窗口不合法：
        #4：移动L指针
        #5:没有经过 while那么窗口就是合法的
        #6:记录数值，让下一轮R进入

        l,r = 0,0
        res = 0
        window = {}
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            while (r-l+1-max(window.values())) >k:# current window is not legitimate so need to make it legitmate and then to count length
                window[s[l]] -=1
                l+=1
            res = max(res,r-l+1) #current window is legtimate after adding 0
        return res


            



