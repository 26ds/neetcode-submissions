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
        # time complexity id O(n)
        # memery coplexityu is O(n/2) ( the biggest numnber of node in a leve is n/2 )


# I need to traverse every single node in the tree
# 1: add the root:
# store every level in a queue
# traverse each level: length of the queue before adding any new children of anode
#memery coplexityu is O(n/2)
# each level is a []
# get the value of a level sequentially: left-> right + remove the value: leftpop()
#add it to the current level
# add the left and right children to the queueue for the next round
        