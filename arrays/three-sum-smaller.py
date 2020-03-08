# https://leetcode.com/problems/3sum-smaller/submissions/
'''
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
'''
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0
        
        nums.sort()
        
        count = 0
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            
            while j < k:
                c = nums[i] + nums[j] + nums[k]
                if c < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1
            
        return count
                    
        
        
        