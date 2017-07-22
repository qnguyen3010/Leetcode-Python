#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:40:01 2017

@author: AaronNguyen
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result

solution = Solution()
array = [1,1,2,2,3,3,4,4,5,6,6,7,7]
print (solution.singleNumber(array))