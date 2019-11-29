"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        flag = 1
        def isb(root: TreeNode):
            if root is None:
                return
            depth = abs(self.max_depth(root.left) - self.max_depth(root.right))
            if depth > 1:
                flag = 0
            isb(root.left)
            isb(root.right)
        return flag


        """
        左子树的最大高度和右子树的最大高度差
        
        :param root: 
        :return: 
        """

    def max_depth(self,root:TreeNode):
        if root is None:
            return 0
        else:
            left = self.max_depth(root.left)
            right = self.max_depth(root.right)

            return max(left,right)+1