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
            #⚠️ len(queue) is changing, need to lock it before changing queue,speicifically finding the  last node: is from 对应i（被循环）的值和 level size：就是循环 2次就到了。（一层两个的话）
            level_size = len(queue)
            for i in range(len(queue)):
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
            
                

        