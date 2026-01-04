# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #1这个题目给我return最长的深度是一个整数
        #2 base case这个走到底是？ 0
        if not root:
            return 0
        
        #3先check还是先走路？他在自己这一层是否可以做出判断，还是要等待下一层child返回的信息？
        #要先跑路，需要等来自child的信息
        left = self.maxDepth(root.left)
        right =self.maxDepth(root.right)
                                #想想自己在中层，此时来自下层的工作已经做好了收集
                                #我们已经有来自左边和右边的深度
        #汇报上一层（boss），boss下面有多高（即我自己层（包括）+我自己层下面的高度）
        return max(left,right)+1