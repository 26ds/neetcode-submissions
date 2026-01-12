# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #一直删除target,且左边右边没人

        if not root:
            return None

        root.left = self.removeLeafNodes(root.left,target)      #✅先看孩子
        root.right = self.removeLeafNodes(root.right,target)

        if not root.left and not root.right and root.val == target:
            return None
        return root