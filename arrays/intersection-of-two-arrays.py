# https://leetcode.com/problems/intersection-of-two-arrays/
'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 and not nums2:
            return []
        
        if nums1 and not nums2:
            return []
        
        if not nums1 and nums2:
            return []
        
        s = []
        result = []
        for i in range(len(nums1)):
            s.append(nums1[i])
            
        for i in range(len(nums2)):
            if nums2[i] in s and nums2[i] not in result:
                result.append(nums2[i])
                
        return result
        
        