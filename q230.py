#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:21:02 2017

@author: AaronNguyen
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        array = []
        self.inorder(root,array)
        return array[k-1]
    
    def inorder(self,root,output):
        if root == None:
            return
        self.inorder(root.left,output)
        output.append(root.val)
        self.inorder(root.right,output)
        
        