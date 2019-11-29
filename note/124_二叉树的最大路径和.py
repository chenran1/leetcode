"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        这个答案只适合与从根节点出发的所有路径
        :param root:
        :return:
        """
        res = []

        def add(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                res.append(root.val)
            if root.left:
                root.left.val += root.val
            if root.right:
                root.right.val += root.val
            add(root.left)
            add(root.right)

        add(root)
        return max(res)