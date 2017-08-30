#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:20:54 2017

@author: AaronNguyen
"""

class Solution(object):
    def twoSum(self,nums,target):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            else:
                dict[target - nums[i]] = i
                
nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums,target))