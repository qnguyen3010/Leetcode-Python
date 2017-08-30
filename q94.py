#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:07:22 2017

@author: AaronNguyen
"""

class TreeNode(object):
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self,root):
        result = []
        self.helper(root,result)
        return result
    
    def helper(self,root,result):
        if root:
            self.helper(root.left, result)
            result.append(root.val)
            self.helper(root.right, result)
            