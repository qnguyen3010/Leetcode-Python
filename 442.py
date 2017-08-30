#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:17:00 2017

@author: AaronNguyen
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        for j in hashmap:
            if hashmap[j] > 1:
                result.append(j)
        return result
    
nums = [4,3,2,7,8,2,3,1]
solution = Solution()
print (solution.findDuplicates(nums))