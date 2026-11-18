# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal
        #   node
        #left.  right       left node right
        self.k =k
        self.res =None

        def dfs(root):
            if not root or self.res:
                return None
            
            dfs(root.left)
            
            self.k -=1.  #一见到你就少一个
            if self.k ==0:# 检查是不是减少没了=0， 从 只有一个 ， k=1 见到你k-=1 所以K成为了0 找到了这个。
                self.res = root.val
            dfs(root.right)
        dfs(root)
        return self.res
        
            

        