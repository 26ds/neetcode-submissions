# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #0这个函数的定义：返回最low最低的可以包含p q as child 的 一个node， p/q可以是node本身
        #1base case
        #2问自己先check还是先跑路recursion
        #       先recursion：因为不管是这个node和p/q的其中一个相等了or没有一个相等，都要往后看一看
        #🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠🧠nobrainer🧠🧠🧠🧠BST就是有的特点：当前节点的左边是比节点小的，右边是比节点大的
        #2想 base case，因为有需要先检查的情况-》先检查
        #靠这道题不仅仅是死板检查而是可以通过当前节点的大小来检查too：
        #case1 如果p q both大于当前node，则看右下方是否可能是commonancesotr
        #case2 如果 pq both 小于，则左下方是否可能是commonancesotr
        #case3/4 如果p/q 其中一个小于节点，一个大于节点，则当前节点就是common ancestor 🌟此乃找到答案了
        #case4/4 如果p/q 其中一个等于节点--》则当前节点就是common ancestor 🌟此乃找到答案了
        if not root:
            return None
        
        #if p.val  == root.val:
           # return root
        #if q.val == root.val:
           # return root
        #if p.val > root.val or q.val >root.val:
            #return root
#🌟因为这三种情况是互斥的（不可能既都在左边，又都在右边），所以用 if ... elif ... else 结构最清晰。
        if p.val> root.val and q.val >root.val:
            return self.lowestCommonAncestor(root.right,p,q) #意思的是往左下去找答案（lowest ancestor）吧
        elif p.val < root.val and q.val <root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        # Case 3: 剩下的所有情况
        # 包括：一左一右、root等于p、root等于q
        # 这些情况不需要写判断了，直接 else 兜底，当前 root 就是答案！
        else:#🌟此乃找到答案了 直接返回当前node
            return root
       











         