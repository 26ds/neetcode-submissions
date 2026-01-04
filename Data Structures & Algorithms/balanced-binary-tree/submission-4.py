# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #0这个函数给我返回一个bool，可是我需要在每一个节点返回整数来比较两边的高度
        status = True
        def heightcheck(root):
            nonlocal status
            if not root:
                return 0
                #1判断一下先recursion还是先return，因为在本父节点必须依赖子节点的汇报，才能知道自己的高度状态
            left = heightcheck(root.left) #此时🌟🧠想象中间节点拿到了左边的高度
            right = heightcheck(root.right)#🧠想象中间节点拿到了右边的高度
            if abs(left - right)>1:
                status = False
                 
            #else:                          可是如果在当前节点就returntrue的话，那么只要有一个达标就结束recursion
            #    return True                后面 有没检查的
            return max(left,right)+1
        heightcheck(root)
        return status