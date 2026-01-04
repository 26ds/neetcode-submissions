# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #不仅仅是特殊input，而且还可以是整个函数的base case：
        #       如果走到最后都没有报错return False，那就是会一层一层往上return True
        if not p and not q:#1 base case:   2 null trees null , nulll 
            return True         
#核心区别：只有“坏人”才配被提前拦截
# --- check阶段 (Work) ---
    # 我现在就能决定要不要把游戏结束掉！
        if not p or not q: #2 base case  1 null and 1 node     
            return  False

        if p.val != q.val:# 3base case  recursion的base case
            return False
             

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
         
        """
        Tree P          Tree Q
        1               1
       / \             / \
      2   3           2   3
     / \ / \         / \ / \
    N  N N  N       N  N N  N  (N 代表 None)
    第一阶段：Root (1) 发包
Root (1) 进来了。值一样。
Root (1) 执行：return isSame(2, 2) AND isSame(3, 3)
它被挂起了，等待左边 2 的结果。
    第二阶段：Node (2) 发包
Node (2) 进来了。值一样。
Node (2) 执行：return isSame(None, None) AND isSame(None, None)
它被挂起了，等待左下角 None 的结果。
        """  
            

        