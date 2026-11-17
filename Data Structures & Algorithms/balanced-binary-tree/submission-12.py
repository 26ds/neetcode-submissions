# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def Balanced(root):
            
            if not root:
                return 0
            left =Balanced(root.left)
            if left ==-1:
                return -1
            right =Balanced(root.right)
            if right ==-1:
                return -1

            if abs(left-right) >1:
                return -1                   #w每一个return都是我这个节点变成了什么（-1），；然后上级会看到我（-1） 如果我在左边：left=我=-1 所以if那就是上级的左边是-1的话：上级就变成-1了
                                            # if我的左边=-1，那么return-1（我就变成了-1）                                              if上级的left ==-1，       return-1
            return max(left,right)+1        #如果我的左边和右边都是-1，那么我不会变成-1，return max +1（我会变成左边/右边的最长的一个+1）
        
        return Balanced(root) !=-1
        
        