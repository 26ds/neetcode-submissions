# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:             #形象的来说现在有：  1
        def check(root):                                                 #               / \
            if not root:                                                #              2     3
                return 0                                               #                      \
            left = check(root.left)     # 1. 拿到左边高度                                        4 
 # if abs(left - right) > 1: return -1   ❌这时候 right 还没算出来                                 \
            if left == -1:                                                                #       5
                return -1
            right = check(root.right)   # 2.拿到右边高度    
            if right ==-1:
                return -1
            if abs(left-right) >1:      #往上报的时候是             在节点3右边高度right =2 ，左边高度为0
                return -1               #                           给1报的时候直接是-1   
                                        #  ，               然后在1节点结算高度时   left = 1（2的高度） 
                                        #                                       right = -1 ->直接return-1                        

#要想比较 left 和 right 的差值（判断平衡），你手里必须同时拥有 left 和 right 两个数据。 
#就像你想比较 我和姚明谁高，你不能只把我的身高量出来就开始比，你必须把我们两个人的身高都量出来，放在桌子上，才能做减法。

            return max(left,right)+1    #左/右边低的时候取最高的一边+上本层
        
        return check(root) !=-1
