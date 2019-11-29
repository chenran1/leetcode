"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def getRow(self, numRows: int):
        if numRows < 0:
            return []
        res = []
        for i in range(numRows + 1):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                tmp = []
                tmp.append(1)
                for j in range(1, i):
                    num = res[i - 1][j - 1] + res[i - 1][j]
                    tmp.append(num)
                tmp.append(1)
                res.append(tmp)
        return res[numRows]
