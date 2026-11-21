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

        
        if p.val < root.val and q.val < root.val:
            left = self.lowestCommonAncestor(root.left,p,q)
            return left
        elif p.val>root.val and q.val> root.val:
            right = self.lowestCommonAncestor(root.right,p,q)
            return right

        # othercases return the root itself
        return root

        #以后每一个root.right/left都会来这个 lowestCommonAncestor()函数里面找一次直到找到为止 
        #写代码的时候就像当前节点：
        #1: 这个函数是干啥的 返回什么
        #2:
        #       root
        #      /    \
        #   left    right
        #3：root 本身返回什么

        