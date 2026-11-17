"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
         # 如果 p 和 q 路径一样长且剩下路径相同时，会直接在 LCA 相遇；一左一右在lca下方
#那么按照一样长的逻辑⚠️如果不一样长，那就让一起走到LCA的路程一样
#                   让先走完的那一方去走另一方的起点，本质是在补齐路程差

#当两个人在循环期间🌟走过的总路程完全一样时，
#他们第一次相遇的位置必然是 LCA

#🌟两条路径的公共部分的起点
#p 和 q 向上走
#🌟在 LCA 之前，路径不重合
#🌟从 LCA 开始到 root，路径完全一样
        a = p
        b=q
        while a!=b:             #while没到LCA后续路径不一样时
            a= a.parent if a else q
            b = b.parent if b else p
        #无论谁先走完,都要回到没走完的那预防陪他走到路径完全一样的那个点
        return a