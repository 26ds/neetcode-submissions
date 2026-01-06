# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #0这个函数返回的是好node的个数
        #一开始的node无论如何都是goodnode因为没人比他大
        #算法：1dfs的时候不断更新最大的就好了：因为题目要求的是“ no nodes with a value greater than the value of node x
        #当前node 比当前node上面的所有node都要大：当前node是最大node
        #     2:更新max value
        #先check还是先跑路？我需要孩子的信息吗？no，我需要的是上面的max信息：所以我需要的是checknow
        if not root:
            return 0
        answer = 0
        

        def count(root,curmax):
            if not root:
                return None
            nonlocal answer
            #Max_val = root.val # ❌ 彻底失忆。每到一个节点都重置标准，不知道祖先是谁，只跟自己比。	❌ 逻辑跑不通
 
        #    nonlocal Max_val# ❌ 坏事就坏在这里，因为左边的兄弟变强了，不应该影响右边的兄弟。
            if root.val >= curmax:
                answer+=1
                curmax = max(root.val, curmax)

            count(root.left,curmax)
            count(root.right,curmax)

        count(root,root.val)

        return answer
        
    





# if not root:
#             return None
#         answer = 1
#         Max_val = root.val

#         self.count(root)

#         return answer
        
#     def count(self,root):
#         # nonlocal answer
#         if root.val > Max_val:
#             answer+=1
#             Max_val = max(root.val,root.val)
#         self.count(root.left)
#         self.count(root.right)


        