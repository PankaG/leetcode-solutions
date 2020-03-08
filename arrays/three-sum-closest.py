# https://leetcode.com/problems/3sum-closest/submissions/

'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return None
        
        nums.sort()
        
        minSoFar = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            
            c = nums[i] + nums[j] + nums[k]
            while j < k:
                if c > target:
                    k -= 1
                elif c < target:
                    j +=1 
                    
                if abs(c-target) < abs(minSoFar-target):
                    minSoFar = c
                
        return minSoFar