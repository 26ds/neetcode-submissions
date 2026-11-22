# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque() # double ended queue
        if root:
            queue.append(root)
        res = []

        while len(queue)>0:
            #each level start with a start new fresh curr_level list
            curr_level = []
            for i in range (len(queue)):
                curr = queue.popleft()
                curr_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # this level end
            res.append(curr_level)
        return res

        