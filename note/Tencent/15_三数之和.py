"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3 :
            return []
        nums.sort()
        numsTmp = []
        res = []
        numsTmp.append(nums[0])
        for i in range(len(nums)-1):
            if  nums[i] == nums[i+1]:
                continue
            numsTmp.append(nums[i+1])
        for num in range(len(numsTmp)):
            L = num -1
            R = num +1
            while L>=0 and R < len(numsTmp):
                if numsTmp[L]+numsTmp[num] + numsTmp[R] == 0:
                    res.append([numsTmp[L],numsTmp[num], numsTmp[R]])
                elif numsTmp[L]+numsTmp[num] + numsTmp[R] < 0:
                    L -= 1
                else:
                    R += 1
        return res