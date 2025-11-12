class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       ###### brute force #######
        # possible_profit=[]
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i] >0:
        #             possible_profit.append(prices[j]-prices[i])
        # if not possible_profit:
        #     return 0
        # else:
        #     return max(possible_profit)
        ###### 2 points search #######
        buy = 0
        sell = 1
        profit = []
        while  sell < len(prices):
            if prices[sell]-prices[buy] >=0:
                profit.append(prices[sell]-prices[buy])
                sell = sell +1
                #profit.append( prices[sell]-prices[buy])
            else:
                buy = sell
                sell = sell +1
        if not profit:
            return 0
        else:
            return max(profit)