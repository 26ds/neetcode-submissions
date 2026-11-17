class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the rows that the target number is in and then do binary search in that row

        ROWS = len(matrix)
        COLOUM = len(matrix[0])

        lCfinder =0
        rCfinder = len(matrix) -1

        while lCfinder<=rCfinder:
            midrow = lCfinder+(rCfinder-lCfinder)//2
            if target>matrix[midrow][-1]:
                lCfinder = midrow+1
            elif target<matrix[midrow][0]:
                rCfinder = midrow-1
            else:
                break
                #we find the row
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