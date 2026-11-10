class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the rows that the target number is in and then do binary search in that row

        ROWS = len(matrix)
        COLOUM = len(matrix[0])

        lCfinder =0
        rCfinder = len(matrix) -1

        while lCfinder<=rCfinder:
            midrow = lCfinder+(rCfinder-lCfinder)//2
            if target>matrix[midrow][-1]: #bigger than the biggest of the midrow
                lCfinder = midrow+1
            elif target<matrix[midrow][0]: #smaller than the smmalles of the midrow
                rCfinder = midrow-1
            else:# in the range of the midrow 
            #matrix[midrow][0] <= target <= matrix[midrow][-1]
                break #we find the row
        #找到了的话l=r 就是输出了 break了（最坏）
        #如果没找到的话 l=r了以后 继续进入循环直到l》r l=r while循环结束后 r<l 还是没找到 再次尝试进入循环
        if not(lCfinder<=rCfinder):
            return False

        l,r = 0,len(matrix[midrow])-1
        

        while l<=r:
            mid = l+(r-l)//2 
            if matrix[midrow][mid] > target:
                r = mid-1
            elif matrix[midrow][mid] < target: 
                l = mid+1

            else:
                return True
        return False