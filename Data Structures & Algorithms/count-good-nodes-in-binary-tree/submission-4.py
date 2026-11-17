# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #每个节点，curmax需要更新，所以需要传参数传下去，
        #               如果比curmax大或者等于，那就总参数gloabl +1
        #先check后recursion

        count = 0
        def helper(root,curmax):
            if not root:
                return None
            nonlocal count
            if root.val >= curmax:
                count+=1
                #curmax只能被带入走进这个number的pat
                curmax = max(root.val,curmax)
            
            helper(root.left, curmax)
            helper(root.right,curmax)
        helper(root,root.val)
        return count
        