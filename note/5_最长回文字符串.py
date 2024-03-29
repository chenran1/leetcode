'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babadwewewewewewewewewwewewewew"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

'''
import time
class Solution:
    def longestPalindrome( s: str) -> str:
        '''
        暴力解题法，列举出所有子串，依次比对是否是回文字符串
        :param s:
        :return:
        '''
        lens = len(s)
        #保存最长回文长度
        l = 0
        #保存最长的回文字符串
        strs = ''
        #cur_l保存当前遍历的长度

        for cur_l in range(2,lens):
            for i in range(0, lens-cur_l-1):
                tmp = s[i:cur_l]
                if Solution.ishuiwen(tmp):
                    if cur_l > l:
                        l = cur_l
                        strs = tmp

        return strs

    def ishuiwen(s:str):
        tmp = s[::-1]
        if tmp == s:
            return True
        else:
            return False

    def longestPalindrome2(self, s: str) -> str:
        '''
        暴力法采用双指针两边夹，验证是否是回文子串，时间复杂度比较高，除了枚举字符串的左右边界以外，比较容易想到的是枚举可能出现的回文子串的“中心位置”，从“中心位置”尝试尽可能扩散出去，得到一个回文串。

        因此，中心扩散法的思路是：遍历每一个索引，以这个索引为中心，利用“回文串”中心对称的特点，往两边扩散，看最多能扩散多远。
        :param s:
        :return:
        '''
        size = len(s)
        if size < 2:
            return s

        # 至少是 1
        max_len = 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    def __center_spread( s, size, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1


start = time.time()
str = 'babadererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereererererererererererererererererererererererereerererererererererererererererererererererereree'
print(Solution.longestPalindrome2(Solution, str))
end = time.time()
print("运行需要的时间为：%.5f"%(end - start))
