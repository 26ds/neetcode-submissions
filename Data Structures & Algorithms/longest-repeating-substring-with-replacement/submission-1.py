class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #其实和上一道题的思路是一样的，只不过我们现在⚠️多了一个复杂度 of 记录多少个可以替换的字母而已
        #⚠️还多了谁被替换是出现的评率决定的，谁的频率不是最高那就是被替换的
        #所以r一直向右移动知道不合法（我们定义的是：窗口长度-最大的频率 = 需要替换以保持一致的数量 > k的时候）
        #左指针l移动到合法 <=k的时候 r就可以继续移动
        #r一直向前，while出故障：l再向前，记下最长

        l = 0
        maxlen = 0
        count = {}#计算每个在窗口内的出现频率
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) >k:#窗口长度-最大的频率 = 需要替换以保持一致的数量 > k的时候
                count[s[l]] -=1
                l+=1
            maxlen = max(maxlen, r-l+1)

        return maxlen


