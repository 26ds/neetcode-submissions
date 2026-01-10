# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 1当前情况就是：如果两个都在左边那肯定就应该在左边着都在右边同理
        #2一左一右：直接是当前节点
        #一个pq自己本身是节点，那就也是当前节点

        #上到下还是bottom up？：
        
        if root.val == p.val or root.val == q.val or  p.val<root.val<q.val or q.val<root.val<p.val:
            return root

        if p.val >root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val <root.val and q.val < root.val:

            return self.lowestCommonAncestor(root.left, p, q)
        

