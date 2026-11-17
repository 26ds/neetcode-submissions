# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #1/7 21:23
        #需要知道孩子先，然后再是回到自己：所以先recursion
        #所以策略是在进行算高度的时候每个几点上报自己的高度之前，更新一下diameter
        #diameter，有可能在任何节点出现，所以我们需要一个全局变量
        maxheight = 0
        def height(root):
            if not root:
                return 0
            nonlocal maxheight
            left = height(root.left) #拿到了左边的高度
            right = height(root.right)#右边的高度  从孩子那里得到信息

            maxheight = max(maxheight, left+right )

            return max(left,right) +1#从B的视角去看B的高度也就是left是怎么来的

        height(root)
        return maxheight