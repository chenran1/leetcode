'''
题目描述

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None: return True
        # 判断两颗子树书否对称
        return self.isSym(self, root.left, root.right)
    def isSym(self, left:TreeNode, right: TreeNode):

        if left == None and right == None: return True
        if left == None or right == None: return False
        # 对称的条件是，1.俩根节点相等。 2.树1的左子树和树2的右子树，树2的左子树和树1的右子树都得是对称的
        return left.val == right.val and self.isSym(left.left,right.right) and self.isSym(left.right, right.left)