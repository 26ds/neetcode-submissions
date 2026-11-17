# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root:
            return False#但是到底了难道不是从底开始往上返回吗 入股obase都是false那不都是false了吗
            #我还是不知道如何去想basecase如何是往上走的 以及如何呼应我的“中间层”
            
        #if still di not find the root of subroot, then it is false

        #need to know the the goal of this function is to return a bool vaule of wheter there is a subtree
        # at the current node: how do i know if the subtree is found
        # 1: found in the left_child's report
        # 2: found in the right_child's report
        # 3: the nodeit self
        # return either of the 3 condition

        left = self.isSubtree(root.left,subRoot)# a bool
        right = self.isSubtree(root.right,subRoot)# a bool

        return left or right or self.issameTree(root,subRoot)

    def issameTree(self,p,q):
        # 这个function
        if not p and not q:
            return True
        if not p or not q:
            return False
        

        left = self.issameTree(p.left,q.left)
        right = self.issameTree(p.right,q.right)

        return left and right and p.val==q.val


