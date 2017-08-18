#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:46:50 2017

@author: AaronNguyen
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)
                
solution = Solution()
print(solution.generateParenthesis(3))