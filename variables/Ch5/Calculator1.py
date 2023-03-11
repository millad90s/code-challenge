# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 01:28:01 2023

@author: user1
"""

def sums(*args):
    return sum(args)

def subtraction(*args):
    result = args[0]
    for i in args[1:]:
        result+=-i
    return result

def multis(*args):
    result = 1
    for i in args:
        result*=i
    return result

def divs(*args):
    result = args[0]
    for i in args[1:]:
        result*=(1/i)
    return result



    

    
