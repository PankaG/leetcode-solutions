# https://leetcode.com/problems/3sum/submissions/

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return None
        
        nums.sort()
        
        result = []
        for i in range(len(nums)-2):
            if nums[i] > 0: 
                break
                
            if i > 0 and nums[i] == nums[i-1]: 
                continue #[1]

            j = i+1
            k = len(nums)-1
            while j < k:
                c = nums[i] + nums[j] + nums[k]
                if c > 0:
                    k -= 1
                elif c < 0:
                    j += 1
                else:
                    r = [nums[i], nums[j], nums[k]]
                    result.append(r)
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return result
                    
            