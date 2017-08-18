#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:31:53 2017

@author: AaronNguyen
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = []
        self.inOrder(root,output)
        for i in range(1, len(output)):
            if output[i] <= output[i-1]:
                return False
        return True
        
    def inOrder(self, root, output):
        if root is None:
            return
        self.inOrder(root.left,output)
        output.append(root.val)
        self.inOrder(root.right,output)