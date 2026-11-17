# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, left , right):

            if not root:
                return True
            if not(left<root.val<right):
                return False
    # it is time to go down , post-order traversal: need to know the children first before going up : the 
    # the node goes all the way down to the最左边的 bottom-left node's left(null)-> returning the ottom left one is T
    # the node then goes to the x.right which is最左边的 bottom left's neighbors-> also return Truw
    # X got True and True from left's(最左边的) bottom left and bottom right 
    #X is true -> X's neighbor..... and 上一层:X i-> X i的neighbor....上一层知道allthewayup
            left = helper(root.left,left,root.val)
            right = helper(root.right,root.val,right)

            return (left and right)

        return helper(root,float("-inf"), float("inf"))

        