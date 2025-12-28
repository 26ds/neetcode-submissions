class Solution:
    def trap(self, height: List[int]) -> int:
        #要找到每个格子的min（左边的max和右边的max）是什么，因为这个min才是给他兜底的
        #我们不需要纠结一个宽度有多少高，我考虑的事每个格子他最多有多高

        #所以每个格子有对应的leftmax和rightmax 建立两个array

        leftmax = [0]*len(height)
        rightmax = [0]*len(height)

        ###错误点，最左/右 边的值一定要加上这个原数列本人：要不然算储水量[i]会算出- 0 -height =负数 - 但我要让这个0变成height
        leftmax[0] = height[0] #处理最左的值
        for i in range(1,len(height)): #最左边没有左边的最大
            leftmax[i] = max(height[i],leftmax[i-1]) #当前这个height的序列，与，上一个数的leftmax（也就是目前收集到的最大） 进行比较谁更大

        rightmax[len(height)-1] = height[len(height)-1] #处理最右的值
        for i in range(len(height)-2,-1,-1): #最右边的没有最大的所以从倒数第二个开始 len -1是倒数第一个
            rightmax[i] = max(height[i],rightmax[i+1])
        
        sum = 0
        for i in range(len(height)):
            sum += min(leftmax[i],rightmax[i])-height[i]
        return sum

        """
        索引 i,高度 H,LeftMax (含),RightMax (含),"min(L, R)",计算: min - H,结果
        0,       3,     3.       ,3.           ,min(3,3)  ,3 - 3,        0
        1,1,3,2,2,2 - 1,1 (存住了!)
        2,       2,     3,        2(height本身),  min(2,3)      ,2 - 2,      0
        """