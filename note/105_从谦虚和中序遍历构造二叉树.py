"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if len(preorder) == 0 :
            return None
        val  = preorder[0]

        del preorder[0]
        in_index = inorder.index(val)
        pre_left = preorder[0:in_index]
        pre_right = preorder[in_index:]

        in_left = inorder[0:in_index]
        in_right = inorder[in_index+1:]
        node = TreeNode(val)
        node.left = self.buildTree(self,pre_left,in_left)
        node.right = self.buildTree(self,pre_right,in_right)
        return node
