'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:

        queue = deque()
        res = []
        if root == None:
            return
        queue.append(root)
        level = 0
        while queue:
            lens = len(queue)
            res.append([])
            for i in range(lens):

                node = queue.popleft();
                res[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return res;


