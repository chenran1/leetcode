"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows < 1:
            return []
        res = []
        for i in range(numRows):
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
        return res
