# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #最后一层的节点约等于所有节点个数的和的一半？所以space complexity是O(n/2)

        #root 是一个“入口”
#👉 通过它，你“能摸到”整棵树
#👉 但 queue 里 只存了这一个节点            root  ──► left ──► left.left ...
                                        #└─► right ─► right.right ...
        #1❌处理空值
        if not root:
            return []
        answer = []
        q = collections.deque()
        
        
        q.append(root)
        while q:
            leng = len(q)
            level = []
            for _ in  range(leng):
                node = q.popleft()
                level.append(node.val)#2❌不是node本身，而是node的值才是int
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            answer.append(level)
        return answer

