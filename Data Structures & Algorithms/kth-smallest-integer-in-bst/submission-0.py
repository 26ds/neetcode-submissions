# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #用一下 BFS把所有的值都加入一下列表，然后和用heap循环k次加入列表，取出最后一个

        q = collections.deque()
        q.append(root)
        everynum = []

        while q:
            leng = len(q)
            # thislevel = []
            for _ in range(leng):
                node = q.popleft()
                everynum.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        mins = []
        heapq.heapify(everynum)

        for _ in range(k):
            mins.append( heapq.heappop(everynum))
        return mins[-1]
            
