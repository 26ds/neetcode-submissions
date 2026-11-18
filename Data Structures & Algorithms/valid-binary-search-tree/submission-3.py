# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # smaller than all subtree and bigger than the right subtree

        def valid(node,left,right):

            #在当前节点 应该想点什么： if current node is in the boundary
            #results of  left child and right child return??? true or false? 
            #current node
            # left and right child

            if not node:
                return True
        #preorder traversal
            if not (left<node.val<right):
                return False
    #child 的
    #left child is smaller than the currentnode
    #right child is  bigger tha the current node
            return (valid(node.left,left, node.val) and valid(node.right,node.val,right))

        return valid(root,float("-inf"),float("inf"))