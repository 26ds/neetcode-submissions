# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #0🌟，因为题目是The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
        #      所以maxDepth（root）的意思就是以这个root为节点左边还是右边最深？--那最深的那一侧长度是多少？

        #1.base case:
        if not root:
            return 0    #return the value of depth  #🌟如果都不是节点（为空）直接return 0，如果为一个“单”父节点，左右都为0，算上本层就是
        
        left = self.maxDepth(root.left)                                  #                                                        ｜
        right = self.maxDepth(root.right)                                #                                                        |
#                                                                    #                                                       |
        maxlen = max(left,right)+1 #本层（算1）和 本层以下的                                                    1+0=1        <---  

        return maxlen