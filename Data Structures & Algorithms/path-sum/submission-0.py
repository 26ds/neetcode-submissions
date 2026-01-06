# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #0这是top down每个节点都应该检查root.val和上面下来的和一不一样：所以先check再recursion
        #函数的定义是否节点给我bool值：所以我认为需要一个helper 函数

        if not root:                                #           A
            return False                            #          / \
                                                    #         B   C
        def helper(root,sumbefore): 
            if not root:        #1base
                return False
            #2自己check+更新
            if (not root.left and not root.right) and root.val+sumbefore == targetSum:
                return True
            sumbefore = sumbefore +root.val
        #3，催下属：左边和右边 
            left =helper(root.left,sumbefore)
            right = helper(root.right,sumbefore)
        #4  A得到下属回应，要给A的上面汇报去了，只要A左下和右下，有一个True就算是有True
            return (left or right) #左边和右边找到都可以
        
        
        return helper(root,0)
        


        