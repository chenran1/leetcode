"""
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        此题其实就是寻找[m,n]范围内二进制数高位（左边）没有变化的数，后面补上0即为所求的结果。

判断m、n是否相等，如果不相等，m+1会使m的二进制数末位进位，有进位说明m的末位肯定有0的情况，0与任何数相与皆得0，所以结果的末位肯定是0。同理，不断右移1位进行比较，直到最终 m=n 时，说明找到了[m,n]这个范围内高位没有变化的数，左移相同位数得到的结果就是所求的值。

        :param m:
        :param n:
        :return:
        """
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        return n<<count