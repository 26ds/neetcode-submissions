# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #0，这个函数的契约是返回我什么？一个最长的diameter
        #算每一个节点的高度的时候，把来自左child和右child的高度加起来就是diameter
        #所以正常算高度，到达每个节点的时候有最高的更新一下就好

        longest = 0

        #此时发现靠：如果每次recursion从上往下的话：longest都会变成0:，所以要把计数的和recursion分开来：
        #1新建一个函数，只在这个函数里recursion
        def height(root):
            #❌忘记nonlocal外面的
            nonlocal longest
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
                #1.5 此时想象自己在中间节点，已经收到了来自左child和右child的高度
                #   所以需要开始算diameter了
            longest = max(longest, left+right)

            return max(left,right)+1 #2 给上一层boss返回我这一层及以下的高度
        #3调用函数
        height(root)
        return longest
