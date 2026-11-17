# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        #先干事情？还是先recursion？ 我自己判断去哪里


        if p.val >root.val and q.val > root.val:
            right = self.lowestCommonAncestor(root.right,p,q)
            return  right#
        
        if p.val <root.val and q.val < root.val:
            left = self.lowestCommonAncestor(root.left,p,q)
            return left
        
        return root