# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #我们需要一个curmax的参数一直传递下去
        #还需要一个全局变量来计数

        count =0 

        def helper(root,curmax):
            #这个函数返回的是是不是比当前的大：
            #先检查当前再往下走 preorder
            nonlocal count
            if not root:
                return False
            
            if curmax <= root.val:
                curmax = max(root.val,curmax)
                count+=1

            helper(root.left,curmax)
            helper(root.right,curmax)
        
        helper(root,root.val)
        return count

                
           
            