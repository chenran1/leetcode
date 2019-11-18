'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''
import time
class Solution:
    def lengthOfLongestSubstring( s: str) -> int:
        '''
        采用滑动窗口的思想
        :return:
        '''
        left = 0
        width = 1
        l = 0
        lens = len(s)
        while True:
            if (left + width) <= lens:
                tmp = s[left:left+width]
                if Solution.hassamekey(tmp):
                    l = width
                    width += 1;
                else:
                    left = left+1
            else:
                break
        return l




    def hassamekey(s:str):

        lens = len(s)
        if lens <= 1:
            return True
        for i in range(0,lens):
            if i == lens -2:
                break
            tmp = s[i+1:lens]
            if tmp.find(s[i]) >= 0:
                return False
        return True
start = time.time()
s = "abcabcbbsdsdokojpajdha;dvsqepqrjfbdalsmdbsvfdvfkwuwdk'aldmf;ksdbfshdqowejnfqd'a;sd,f;alsjdvkfjkvbsmdq;oejoenfadskla'd,c;a.kjfds"
#print(Solution.hassamekey(s))
print(Solution.lengthOfLongestSubstring(s))
end = time.time()
print("解决问题所用的时间为：%.5f秒"%(end-start))