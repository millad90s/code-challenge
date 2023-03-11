# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 00:55:50 2023

@author: user1
"""

import sympy

x, y = sympy.symbols('x y')

def calculator():
    while True:
        expr = input("Enter an expression to evaluate (or 'quit' to exit): ")
        if expr == 'quit':
            break
        try:
            result = eval(expr)
        except:
            print("Invalid expression.")
        else:
            print(f"Result: {result}")

calculator()
