class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #水的多少是通过：两个index之间的距离，和这两个index的值min
        #我的思路：先找到两个最高的height的值
                #然后再找他们之间index的差值
        
        #这个思路是错的：
        #使用双指针 ：因为更小的高度时巨献，所以每次往里面移动的时候，对比l r的对应的值：移动小的高度的那一方for higher 高度
        
        l,r = 0, len(heights)-1
        maxA = 0
        while l<r:
            area = min(heights[l],heights[r])*(r-l)
            maxA = max(maxA, area)
            #推进双指针*必要：
            if heights[l]<heights[r]:
                l +=1
            else:
                r -=1
            
        return maxA
        
        