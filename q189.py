#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:16:09 2017

@author: AaronNguyen
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

solution = Solution()
nums = [1,2,3,4,5,6,7]
solution.rotate(nums,3)
print(nums)        