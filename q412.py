#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:31:36 2017

@author: AaronNguyen
"""

class Solution(object):
    def fizzbuzz(self,n):
        return ["Fizz" * (not i%3) + "Buzz" * (not i%5) or str(i) for i in range(1,n+1)]
    
solution = Solution()
print(solution.fizzbuzz(15))