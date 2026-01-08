# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #1/7
        #this function will return if the tree is balanced or not(true/false)
        # but i need integer to keep track the balance condition of each root
        if not root:
            return True
        
        def checkheight(root):
            if not root:
                return 0

            left = checkheight(root.left)
            if left == -1:  #left child is not legit
                return -1
            right = checkheight(root.right)
            if right == -1:
                return -1

            if abs(left-right) >1: #nont legit
                return -1
            else:
                return max(left,right)+1

        return checkheight(root) != -1
        

            
            