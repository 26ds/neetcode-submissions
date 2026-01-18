# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        status =True
        def Balanced(root):
            nonlocal status
            if not root:
                return 0
            left =  Balanced(root.left)
            right = Balanced(root.right)
            if abs(right-left) >1:
                status = False   
                return False
            return max(left,right) +1
        Balanced(root)
        return status
        