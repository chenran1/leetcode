"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def spiralOrder(self, matrix):
        res = []
        left, right, top, buttom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= buttom:
            for i in range(left, right):
                res.append(matrix[top][i])
            for i in range(top, buttom):
                res.append(matrix[i][right])
            if left < right and top < buttom:
                for i in range(right, left, -1):
                    res.append(matrix[buttom][i])
                for i in range(buttom, top, -1):
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            buttom -= 1
        return res

print(Solution.spiralOrder(Solution,[[1,2,3],[4,5,6],[7,8,9]]))

