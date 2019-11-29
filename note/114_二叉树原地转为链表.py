"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(root:TreeNode):
            while root == None: return
            helper(root.left)
            helper(root.right)#后续遍历
            if root.left != None:
                pre = root.left#指向左子树

                while pre.right: pre = pre.right#pre指向左子树的最右子树

                pre.right = root.right #将左子树的最右子树指向root的右子树
                root.right = root.left #将root的右子树指向左子树
                root.left = None #root的左子树置为None

        helper(root)