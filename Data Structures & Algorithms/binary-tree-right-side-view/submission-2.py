# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #只从右边看能看到谁？
        #所以用到Breadth first search：只添加每一层的最后一个
        if not root:
            return []
        answer = []
        q = collections.deque()
        q.append(root)

        while q:
            last_val = 0
            leng = len(q)
            for _ in range(leng):
                node = q.popleft()
                last_val = node.val # 🌟不断更新，直到这一层最后一个
                if node.left:#入queue
                    q.append(node.left)
                if node.right:#入queue
                    q.append(node.right)
            answer.append(last_val)
        return answer


        