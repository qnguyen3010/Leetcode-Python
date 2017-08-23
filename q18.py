#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:25:28 2017

@author: AaronNguyen
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNsum(nums,target,4,[],results)
        return results
    
    def findNsum(self,nums, target, N, result, results):
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
            return
        if N == 2:
            l , r = 0, len(nums)-1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    results.append(result + [nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                    self.findNsum(nums[i+1:],target - nums[i],N-1,result+[nums[i]],results)        
        return        
    
solution = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(solution.fourSum(nums,target))