class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #上一道题是检查重复
        #这一道题是看最多可以重复几次
        #限制1： only uppercase english chara≤　模拟bvcxcters
        #限制2:  an integer k 可以替换k次字母.。 
        #       找最长的连续的 一个字母的string

        #最直接的方法：一个一个试谁是不被替换k次的主元：
        #为什么想到🌟？因为难题就是这么多不同元素

        maxlen = 0
        centers = set(s)
        for center in centers:      #每个元素都要被试一次是不是主元
            l = 0
            count  = 0               #看看这个被考虑的主元出现了几次
            
            for r in range(len(s)):
                if s[r] == center:   #在推动的过程中遇到了当前主元
                    count +=1
                #废话点 2 else:                   #遇到的不是主元
                #显式地写了“如果合法就跳过”  if (l-r+1 - count)<=k:#需要被替换的元素的个数（非主元个数）
                #        continue
                #    else:               #保证窗口合法

                while (r-l+1 - count)>k:
                    if s[l] == center:
                        count -=1   #如果当前s[l]就是主元，那就先减掉它，调整while条件
                    l+=1            #再让窗口继续滑动
                maxlen = max(maxlen, r - l + 1)
        return maxlen
                            


        
