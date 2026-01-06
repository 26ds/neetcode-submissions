# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #但其实要每个做节点的都要比根小，每个右节点的都要比根大
        #所以大小限制范围要跟新，所以需要传递参数和跟新参数
        #0本函数返回bool告诉这个root是不是BST
        #1先recursion还是先check？
        #                   ✅
        if not root:
            return True

        def check(root, left,right):
            if not root:
                return True
                #先check
            if not(left < root.val <right) :          #如果正确 往下recursion⬇️
                return False                        #   否则return False
                #check完毕  
                #向下属要信息                                 #🌟可不可以？？？？这样-🌟
            left = check(root.left,left,root.val)            #   如果不正确（不在范围之间）：
            right = check(root.right, root.val,right)         #   直接return False
                                                        #能到这一步的都是正确的：向下递归
           #🌟 向上汇报，想象check函数会给left函数一个bool值
           #        这道题中必须要left和right之间都是True才可以
            return (left and right)
            
        return check(root, float("-inf"),float("inf"))
        