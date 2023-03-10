# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 01:28:01 2023

@author: user1
"""

def sum_cal(*args):
    return sum(args)

def multiplication(*args):
    result=1
    for i in args:
        result*=i
    return result
