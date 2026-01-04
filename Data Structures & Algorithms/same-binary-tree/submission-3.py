# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #1 base case:   2 null trees null , nulll 
        #2 base case  1 null and 1 node

        

        status = True
        def check(p,q):
            nonlocal status
            if not p and not q:
                return 
            if not p or not q:
                status =False
                return  
            if p.val != q.val:
                status =False
                return 
            check(p.left, q.left)
            check(p.right, q.right)
        check(p,q)
        return status

        