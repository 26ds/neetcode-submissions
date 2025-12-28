class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]>target: #那第m个list的第一个都比target大那么所有右边，包括第m个list本身都肯定
                r=m-1               #(✅target比最小的小 ）                  #不包括target
            elif matrix[m][len(matrix[m])-1] <target:#（✅target比最大的大，那你肯定就在下一个m了
                l= m+1
            else:###错误点❌###这mlist里面的l和r不能和外面的l，r用同一个变量，否则找不到target的话会永远结束不了最外层的循环
                in_l = 0 ###错误点❌###是index不是具体的数
                in_r = len(matrix[m])-1
                while in_l <= in_r:             #在这个确定的m  list去使用binarysearch again去找target
                    in_m = (in_l+in_r)//2
                    if matrix[m][in_m] >target:
                        in_r = in_m -1
                    elif matrix[m][in_m] < target:
                        in_l = in_m +1
                    elif matrix[m][in_m] == target:
                        return True
                return False
###错误点❌###如果找到了所在的m list（行），但是在这里面没有找到目标，程序回到了外层 while 的开头。然后也没有更新l和r，那么外循环就一直不会结束
        return False ###注意点###所在内层（行）都没找到❌
                        #          这一行没的话，找不到行的时候就会返回None





#所以要考虑：1:找得到所在内层✅内层找得到✅；2:找得到所在内层✅，但是具体数没找到❌（里面else后面的false）
#          所在内层（行）都没找到❌（外层后面的false）


"""
很多同学会误以为双层循环就是乘法 O(logm×logn)，但在你的代码里，逻辑是这样的：

先找行（外层循环）： 你在 m 行中进行二分查找。这一步最多花费 O(logm)。

锁定行后（else 块）： 一旦你锁定了某一行（进入了 else），你只会在这一行里做一次二分查找，然后代码就结束了（要么 return True，要么 return False）。这一步花费 O(logn)。

总耗时： O(logm)+O(logn)=O(log(mn))。
"""
