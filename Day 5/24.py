# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:52:53 2020

@author: saura
"""
'''
Question 24
    Python has many built-in functions, and if you do not know how to use it,
    you can read document online or find some books. But Python has a built-in 
    document function for every built-in functions.
    Please write a program to print some Python built-in functions documents,
    such as abs(), int(), raw_input()
    And add document for your own function
Hints:
The built-in document method is __doc__
'''

def cool_func(num):
    '''
    Parameters
    ----------
    num : int
        it is just a number.

    Returns
    -------
    return True if the num is greater than 0, False otherwise
    '''
    if num > 0:
        return True
    return False

print(cool_func.__doc__)
print(str.__doc__)