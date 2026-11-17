# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #返回的事bool，那么需要一个helpoer来计算sumbefore是多少
        
        def helper(root,currsum):
            if not root:
                return False

            currsum = root.val+currsum
            if not root.left and not root.right and currsum == targetSum:
                return True
            
            
            left = helper(root.left,currsum)
            
            if left:  
                return True
            right =  helper(root.right,currsum)
            if right:
                return True
            return False

        return helper(root,0)