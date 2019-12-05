"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        threadth = (1<<31)-1 if x > 0 else 1>>31
        res = 0
        while y > 0:
            res = res * 10 + y % 10
            if res > threadth:
                return 0
            y //= 10

        return res  if x > 0 else -res