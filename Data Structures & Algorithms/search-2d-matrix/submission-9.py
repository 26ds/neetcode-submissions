class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        long = len(matrix[0])#长：length of a list in the list
        width = len(matrix)# 宽，几个list in the list

        l=0
        r=width - 1
        while l<=r:
            mid = (l+r)//2
            if target > matrix[mid][long-1]:
                l = mid+1
            elif  target < matrix[mid][0]:
                r = mid -1
            else:#找到了所在的方块
                l2 = 0
                r2 = long-1
                while l2<=r2:
                    mid2 = (l2+r2)//2
                    if target > matrix[mid][mid2]:
                        l2 = mid2+1
                    elif  target < matrix[mid][mid2]:
                        r2 = mid2-1
                    else:
                        return True
                return False#✨⚠️如果找到了大概但是没有找到具体的，那就是没有了
            
        return False#注意，连最外层的也没有找到
