# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #0这个函数会给我一个bool旨在检查是否两棵树完全相等
        #我们一次有两个argument
        #1base case
        #2思考我们应该先跑路还是先check：
        #       先check
        if not p and not q: #顺序很重要❌出错点
            return True
        if not p or not q:#'NoneType'  先把他们都给出完，如有困惑，看前面submission记录解释
            return False
        if p.val != q.val:
            return False
        
        
        #先check完毕,也该recursion了
        #即当前节点我已经没事了，应该return下一个节点(左边和右边)recursion，让他们看看有没有事

        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

        