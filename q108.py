#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:32:52 2017

@author: AaronNguyen
"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = Node

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        start = 0
        end = len(nums) - 1
        return self.helper(nums,start,end)
    
    def helper(self,nums,start,end):
        if start > end:
            return
        mid = (start+end)/2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums,start,mid-1)
        node.right = self.helper(nums,mid+1,end)
        return node