class Solution:
    def trap(self, height: List[int]) -> int:
        # min(leftmax,rightmax)-height[i] =
        
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)
        
        leftmax[0] = height[0]
        for i in range(1,len(height)):
            leftmax[i] = max(height[i],leftmax[i-1])
        
        rightmax[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            rightmax[i] = max(height[i],rightmax[i+1])
        
        sumrain = 0
        for i in range(len(height)):
            sumrain += min(leftmax[i],rightmax[i])-height[i]

        return sumrain