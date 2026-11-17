class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        possible_profit=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i] >0:
                    possible_profit.append(prices[j]-prices[i])
        if not possible_profit:
            return 0
        else:
            return max(possible_profit)