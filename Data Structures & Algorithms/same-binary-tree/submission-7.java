/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        //顺序很重要不可以把val放在前面要把需要排除的：null放在前面
        //因为我们不可以在这个node可能是null的情况下 去说if p.val != q.val null.val不行啊
        if(p == null && q == null){
            return true;
        }
        if(p == null || q == null){
            return false;
        }
     //   if(p ==  q == null){
     //       return true;
     //   } 为什么不可以这么写：因为只当前节点是一样的就反return true了
     //但是如果是两棵树有一个不一样的地方就可以提前退出了，否则就要dfs到null（底）
        if(p.val != q.val){
            return false;
        }

        return ( isSameTree(p.left,q.left)&&isSameTree(p.right,q.right));
        
    }
}
