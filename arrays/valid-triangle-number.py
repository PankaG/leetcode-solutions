# https://leetcode.com/problems/valid-triangle-number/submissions/
'''
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
'''
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        c = 0
        n = len(nums)
        nums.sort()
        for i in range(n-1,1,-1):
            lo = 0
            hi = i - 1
            while lo < hi:
                if nums[hi]+nums[lo] > nums[i]:
                    c += hi-lo
                    hi -= 1
                else:
                    lo += 1
        return c
                