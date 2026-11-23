# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
             return []
            
        queue = deque([root])

        res = []
        # we need to traverse every node  Breadth frist search for every level, so 
        # Just add the last node of the queue to the res

        while len(queue)>0:
            #⚠️ len(queue) is changing while enqueue,   at the start of each level, i will snapshot  level_size so that  I know eactly how many nodes in this level and wheere is the last node 
            level_size = len(queue)
            for i in range(len(queue)): # pop the level_size times until the last node is popped and recorded
                curr = queue.popleft()
                #the last node
                if i == level_size-1:
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # for loop ends this level of queue ended and next level of queue is loaded ready to go 
        return res
            
                

        