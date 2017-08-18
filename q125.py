#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 23:04:55 2017

@author: AaronNguyen
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right :
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

solution = Solution()
s = 'A man, a plan, a canal: Panama'
S = 'race a car'
print(solution.isPalindrome(s))
print(solution.isPalindrome(S))