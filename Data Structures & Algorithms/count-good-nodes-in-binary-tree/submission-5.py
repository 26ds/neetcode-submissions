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
            newmax = max(root.val,curmax)#需要放在if外面，不管大于还是小于都要更新newmax
            
            helper(root.left, newmax)
            helper(root.right,newmax)
        helper(root,root.val)
        return count
        