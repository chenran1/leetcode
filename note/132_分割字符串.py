"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def minCut(self, s: str) -> int:
        res = float("inf")
        if s == s[::-1]:
            return 0
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                res = min(self.minCut(s[i:])+1, res)
        return res