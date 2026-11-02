class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        #限定条件：1:时间一直往前走不能把今天买的昨天卖掉
        #2:要一直最大的prices

        #sliding window:
        #1:什么时候动左指针？：左指针的意思是买入的时间；移动左指针想要换一个买入时间：那就是更低的买入时间。当R比L小的时候那就需要把L放到R的位置。因为一路过来R都大于L
        L,R = 0,0
#[10,3,5,6,1,9]
#    L,  R           res =3
#    L,    R         R>L:  
        res = 0

        for R in range(len(prices)):
            if prices[L]> prices[R]:
                L=R
            res = max(prices[R]- prices[L],res)
        return res


