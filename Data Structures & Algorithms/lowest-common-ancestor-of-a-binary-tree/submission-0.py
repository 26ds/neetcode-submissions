# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #如果是一个root等于其中一个 pq 的花直接返回这个 root，#而且一大一小在这里不可以了
        # 1. Base Case / 你的 "Pre-order" 检查部分
        # 如果 root 为空，或者 root 就是 p 或 q 本身
        # 我们直接返回 root。
        # 这里的关键是：如果 root 是 p，我们不需要再往下找 q 了。
        # (因为如果 q 在 p 下面，LCA 就是 p；如果 q 在别处，p 会被传上去等待和 q 汇合)
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        #我作为上报点：
        if left and right:
            return root
        
        if left:
            return left
        
        if right:
            return right

        return None
