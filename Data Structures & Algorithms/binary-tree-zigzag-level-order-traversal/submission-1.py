# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        x=0
        output = []
        while q:
            len_q = len(q)
            level = []
            for _ in range(len_q):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if x % 2== 0:
                output.append(level)
            else:
                zig = level[::-1]
                output.append(zig)
            x +=1
        return output