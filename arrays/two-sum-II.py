# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers or len(numbers) < 2:
            return None
        
        result = [None]*2
        m = {}
        for i in range(len(numbers)):
            if target - numbers[i] in m:
                result[0] = m[target - numbers[i]]+1
                result[1] = i+1
            
            m[numbers[i]] = i
        
        return result