class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #注意顺序：只能右边减左边：
        #先建立金库max = 0
        #利用双指针：如果r-l是小于0:则l注定是太大了，更换l看看有没有更小的l
        #         ：如果r-l大于0:
        #.
        #.
        #.
        #.
        #错误❌：“从两端向中间逼近”的双指针算法中，我们必须有一个明确的逻辑来
        #       决定是 L++ (左指针右移) 还是 R-- (右指针左移)。
        #。      这个逻辑必须保证：舍弃的一边绝对不可能是最优解的一部分0

        #需要🌟同时找到🌟最低买入和🌟最高卖出，且
        #所以需要从左往右看，由于一直在移动pointers，所以需要记录下来leftr/right的利润
        l=0
        r=1
        maxp = 0
        while r <len(prices):
            if prices[l] >= prices[r]:
                l=r
                r+=1
            else:
                maxp = max(maxp,prices[r] - prices[l])
                r+=1
        return maxp