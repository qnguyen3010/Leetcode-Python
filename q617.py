#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:54:22 2017

@author: AaronNguyen
"""

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self,t1,t2):
        if not t1 or not t2:
            return None
        t = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        t.left = mergeTree(t1.left if t1 else None,t2.left if t2 else None)
        t.right = mergeTree(t1.right if t1 else None,t2.right if t2 else None)
        return t
    