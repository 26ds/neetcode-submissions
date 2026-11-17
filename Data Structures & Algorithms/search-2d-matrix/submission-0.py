class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        smallvalue_row = 0
        highvalue_row =len(matrix)-1

        while smallvalue_row <= highvalue_row:
            mid_row = (smallvalue_row+highvalue_row)//2
            #（mid大，大的变小且-1）mid中间值这一行的第一个数大了-->mid此行与mid后面的行都不合格；highvalue_row变成了mid_row-1
            if target  < matrix[mid_row][0]:
                 highvalue_row = mid_row -1
            #（mid小，小的变大且+1）mid中间这一行的最后一个数都小于target：
            #那证明target比mid这一行所有的值都大：即target比mid这一行和比mid小的行都大
            #所以smallvalue_row变成了mid +1
            elif target  > matrix[mid_row][-1]:
                smallvalue_row = mid_row+1
            else:#就在此行内 mid row确定下来
                break
                #比如target是10.5咋办，新的针对这一行binary search开始了#
                #mid_row确认下来
#################可如果target是20万怎么办，那就：不是break的情况，而是while循环完了也没找到################
        #最后一次while输出的small和high value一定是不能让while循环的大小，所以while才不会继续循环下去
        #所以small会比big大：    
        if smallvalue_row > highvalue_row:
            return False
        the_row = matrix[mid_row]#新binary search对应的row
        bottom = 0
        top = len(the_row)-1 ###每次都忘记
        while bottom<=top:
            mid = (bottom+top)//2
            if target < the_row[mid]:
                top = mid -1
            elif target > the_row[mid]:
                bottom = mid +1
            elif target == the_row[mid]:
                return True
        return False
        
