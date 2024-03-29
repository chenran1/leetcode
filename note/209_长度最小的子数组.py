"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def minSubArrayLen(self, s: int, nums):
        left = 0
        lens = float("inf")
        value = 0
        right = 0
        while right<len(nums) and left<=right:
            value += nums[right]
            if value >= s:
                print(value)
                print("left:"+str(left))
                lens = min(lens,right - left +1)
                value -= nums[left]
                left += 1

                print(str(lens)+"+"+str(value))
            else:

                right += 1
                print(lens)
        return lens

print(Solution.minSubArrayLen(Solution,7,[2,3,1,2,4,3]))
