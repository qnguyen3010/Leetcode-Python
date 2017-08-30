#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:21:47 2017

@author: AaronNguyen
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n-n//2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j],matrix[j][~i] = matrix[~j][i],matrix[~i][~j],matrix[j][~i],matrix[i][j]
                           
A = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

solution = Solution()
print(A)
solution.rotate(A)
print(A)