# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #第一步现在的isSubtree的含义在我写了checksub函数之后就是check每一个root是不是和苏包容哦天的那个根相等
        if not root:
            return False #第二步base case 如果到最后都没有触发if root == subRoot那么就是false
        #第三步helper
        def checksub(root,subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False
            return (checksub(root.left,subroot.left) and checksub(root.right,subroot.right))
        #第四步先 check再recursion，不需要child的信息,如果触发到且相等就会直接return True
        if root.val == subRoot.val:         # ❌1 错误原来写的是root == subRoot 比较的是这两个对象在内存里是不是同一个对象
            if checksub(root,subRoot):# 如果核对成功
                return True           # 那才真的是找到了

            #return checksub(root,subroot)   ##❌2 如果root相==触发：但是后面不相等我直接return checksub(root,subroot)的话
                                            #就会return False，checksub和isSubtree都不会往下走了 如果“这个人”不是，你应该继续往后找（去左边找，去右边
        #开始recursion

        ##❌3return self.isSubtree(root.left,root.right):里的 subRoot 是那张**“通缉令”**。通缉令是永远不会变的！我们要拿着这张通缉令，去左边找，或者去右边找。
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

         
        