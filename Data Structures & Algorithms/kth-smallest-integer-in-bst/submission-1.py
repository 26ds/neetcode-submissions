# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #如果用DFS，那就是
        #binarytree是 sorted tree,用中序排列，1让左兄弟去干 2.自己直接干 3. 让右兄弟去干
        #                                   -> 让左兄弟加入了列表
        #                                               ->自己加入了列表
        allnums = []
#🌟     没错，这就是中序遍历（In-Order）的铁律：只要左边还有人，我就得等着；等左边搞定了，我才能进名单；最后才轮到右边。
        def recur_through(root):
            if not root:
                return None
            nonlocal allnums
            
            recur_through(root.left)#本人命令左下节点去找一遍，并且坚信这个函数会把 root.left全部先加入allnums
            allnums.append(root.val) #本人就在这一层，直接把本节点加入
            recur_through(root.right)
            
        recur_through(root)

        return allnums[k-1]