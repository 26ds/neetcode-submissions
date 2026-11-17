# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #0🌟，因为题目是The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
        #      所以maxDepth（root）的意思就是以这个root为节点左边还是右边最深？--那最深的那一侧长度是多少？

        #1.base case:
        if not root:
            return 0    #return the value of depth  #🌟如果都不是节点（为空）直接return 0，如果为一个“单”父节点，左右都为0，算上本层就是
        
        left = self.maxDepth(root.left)#🌟(以当前 root 为节点的)左子树的最大深度（一个整数                                         ｜
        right = self.maxDepth(root.right)                                #                                                   |
#                                                                    #                                                       |
        maxlen = max(left,right)+1 #本层（算1）和 本层以下的                                                    1+0=1        <---  
        #✅ 标准、准确、够用的一句话答案是：
    #🌟是“递归函数的返回值 + 每一层固定的 +1”在帮你记住层数。
    #我只在“最小情况”看清楚，
#然后相信所有更大的情况都是由它叠加出来的。
        return maxlen


        """
问题 5️⃣（区分 Tree vs Linked List，关键）
为什么在 Tree 的 maxDepth 里：
return max(left, right) + 1
而在 Linked List 里我们通常是：
return 1 + dfs(node.next)
                    正确的一句话版本（你以后用这个）
            本质区别是：
            Tree 是“分叉结构”，一个节点有多个子问题（left / right），
            而 Linked List 是“线性结构”，每个节点只有一个子问题（next）。
        """