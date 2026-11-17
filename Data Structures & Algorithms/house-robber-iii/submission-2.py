# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        def w_out(root):
            if not root:
                return [0,0]
            
            left = w_out(root.left)#存进了变量好这样就不用在再withoutroot的时候再call一次了，如果携程第一次提交的样子会导致2^n
            right = w_out(root.right)#因为root.left right 会被call两次
            
            withroot = root.val + left[1] + right[1]
            withoutroot = max(left) + max(right)

            return [withroot,withoutroot]
        
        return max(w_out(root))