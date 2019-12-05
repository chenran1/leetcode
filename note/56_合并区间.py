"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        利用快排进行排序，然后进行比较
        :param intervals:
        :return:
        """
        if not intervals:
            return
        def quicksort(intervals,m,n):
            lable = intervals[m][0]
            i, j = m, n

            while i<j:
                while i<j and intervals[j][0] >= lable:
                    j -= 1
                intervals[i] = intervals[j]
                while i<j and intervals[i][0] <= lable:
                    i += 1
                intervals[j] = intervals[i]

            quicksort(intervals,m,i-1)
            quicksort(intervals,i+1,n)
        # quicksort(intervals,0,len(intervals)-1)
        intervals = sorted(intervals)
        res = []
        res_low = intervals[0][0]
        res_high = intervals[0][1]
        for i in range(1,len(intervals)):
            if res_high >= intervals[i][0]:
                if res_high >= intervals[i][1]:
                    continue
                else:
                    res_high = intervals[i][1]
            else:
                tmp = [res_low,res_high]
                res.append(tmp)
                res_low = intervals[i][0]
                res_high = intervals[i][1]
        tmp = [res_low,res_high]
        res.append(tmp)
        return res


