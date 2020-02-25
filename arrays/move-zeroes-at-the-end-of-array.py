# https://leetcode.com/problems/move-zeroes/

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        
        for i in range(len(nums)):
            if nums[i] == 0:
                # Find the next non-zero element to be replaces with zero
                j = i+1
                while j < len(nums):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    else:
                        j += 1
        
        def moveZeroesFaster(self, nums):
            if not nums:
                return None
            
            zero = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i], nums[zero] = nums[zero], nums[i]
                    zero += 1
                    
                
                
    
        
                    
        
        