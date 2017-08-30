#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:20:40 2017

@author: AaronNguyen
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return False
        
        stack = []
        dict = {'}':'{',']':'[',')':'('}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        
        return stack == []

solution = Solution()
s1 = '()[]{}'
s2 = ''
s3 = '(('
print(solution.isValid(s1))
print(solution.isValid(s2))
print(solution.isValid(s3))