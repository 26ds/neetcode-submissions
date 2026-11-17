class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #固定窗口方法：
        #🌟：先进后出：r的移动范围是s1的最后一个index ） 到s2的最后一个index包括
        #先进入右指针再踢出老指针
        lens1 = len(s1)
        lens2= len(s2)
        check1 = [0]*26
        check2 = [0]*26
        
        for i in range(lens1):
            check1[ord(s1[i])-ord('a')] +=1
        
        #是check2“初始化只吃第一口（前lens1个），后面每一步都是吐一口旧的，吃一口新的。”
        #就比如有s1:bcd
        #       s2:febcd   这一步只会让s1有check1 [0 111 000000..0]开头的0加上其他的0共23个是一开始就初始化的
#窗口开始
        l=0
        for r in range(lens2):
            #右边从0进来了：开始核对：
            #在核对了不超过lens1的时候不移动左指针
            check2[ord(s2[r])-ord('a')] +=1
            if r>=lens1:                #比如lens1是长度3，但是当r是3，l到r包含的数就已经是3-0+1=4个了，所以=lens1那一刻起就要开始踢人了
                #l +=1错误❌
                check2[ord(s2[l])-ord('a')] -=1
                l +=1       #“🌟先踢人，再移指针”（
            if check1 == check2:
                return True
        return False

            



         