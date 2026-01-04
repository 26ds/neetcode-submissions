# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diamter = 0
        # if not root:
        #     return 0
        
        #right =  diameterOfBinaryTree(root.right)
        #left =  diameterOfBinaryTree(root.left)

        #eturn right + left 
# ❌ 你把“左子树里 的直径”加上“右子树里的直径”，这在几何上是没有意义的。这两条线可能离得很远，根本连不起来！

# ✅正确的几何逻辑：我先算出左右子树的高度，左右高度相加就是经过这个节点的直径，更新全局最大值；然后返回高度给上一层
#  正常算高度，顺便在回上一层之前算一下 diameter
# 下属先跑（递归调用）。
#拿到下属数据。
#处理当前层逻辑（在这里更新全局 res）。
#向上级汇报（Return 高度）。
        
        def diam_height(root):
            nonlocal diamter
            if not root:
                return 0
            left =  diam_height(root.left)
            right =diam_height(root.right)
            diamter = max(diamter,left+right) #在返回下一层前先更新一下左边+右边的长度

            return max(left,right) +1
        diam_height(root)

        return diamter






