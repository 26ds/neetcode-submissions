# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left                            #root.left我按照常理想应该直接是=root.right
        #                                           因为你在递归里，必须遵守一个铁律：
                                        #❗当前层 永远不能假设子树已经处理好#❗️除非你是通过递归函数拿到的
                                        #                           root.right ❌ → 原始子树（脏的）
#                                                       invertTree(root.right) ✅ → 干净、处理好的子树

        root.left = self.invertTree(root.right) #你脑子里立刻翻译成一句中文：“把已经翻转完成的右子树，接到左边”
        root.right  = self.invertTree(temp)     #“把已经翻转完成的左子树，接到右边”
        """
        invertTree(x)
        返回的是：
        👉 一个「已经被完整翻转好的、以 x 为根的子树」
        三、只做一件事：
站在 root = 1 这一层，不往下模拟
你现在在 root = 1，代码是：
temp = root.left        # temp = 2
root.left = invertTree(root.right)
root.right = invertTree(temp)
按我们刚刚“钉死”的定义翻译成中文👇
invertTree(root.right)
👉 返回：以 3 为根、已经翻转好的子树
invertTree(temp)
👉 返回：以 2 为根、已经翻转好的子树
然后你做的是：
左边 ← 翻转好的 3
右边 ← 翻转好的 2
📌 这一步完全不需要你知道 2 和 3 内部怎么翻的
        """

        return root