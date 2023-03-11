# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:43:37 2023

@author: user1
"""

def calc(a,b,operator):
    result=0
    if operator=='+':
        result = a+b
    elif operator=="-":
        result = a-b
    elif operator=='*':
        result = a*b
    elif operator=="/":
        result = a/b
    else:
        return
    return result
while True:
    print('For calculator: insert two number and one operator')
    print('operator is include: '+'\n'+'sum: + '+'\n'+'substract: - '+'\n'+'multiplication: * '+'\n'+'Division:/')
    print('for Exit: insert 0 in operator')
    

    operator=str(input('Insert a operator for calculator= '))
    if operator=='0':
        break
    a=float(input('Insert first number= '))
    b=float(input('Insert seccond number= '))
    print('result: ',a,operator,b,' = ',calc(a, b, operator))


