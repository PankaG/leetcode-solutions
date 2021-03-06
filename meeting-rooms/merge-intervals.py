# https://leetcode.com/problems/merge-intervals/

'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return None
        
        intervals = sorted(intervals, key=lambda x:x[0])
        result = []
        j = 0
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[j][1]:
                result[j][1] = max(result[j][1], intervals[i][1])
            else:
                result.append(intervals[i])
                j += 1
        
        return result