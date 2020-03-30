# https://leetcode.com/problems/valid-palindrome/

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        i = 0
        j = len(s)-1
        while i < j:
            if not s[i].isalnum() or s[i] == ' ':
                i += 1
                continue
                
            if not s[j].isalnum() or s[j] == ' ':
                j -= 1
                continue
            
            if lower(s[i]) == lower(s[j]):
                i +=1 
                j -= 1
            else:
                return False
        
        return True
                
            