# https://leetcode.com/problems/meeting-rooms-ii/
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
            
        start.sort()
        end.sort()
        
        available = numOfRooms = 0
        s = e = 0
        while s < len(start):
            if start[s] < end[e]:
                if available == 0:
                    numOfRooms += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1
        
        return numOfRooms