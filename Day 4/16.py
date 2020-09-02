# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:14:22 2020

@author: saura
"""
'''
Question 16
    Use a list comprehension to square each odd number in a list. 
    The list is input by a sequence of comma-separated numbers.
    Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9
    Then, the output should be: 1,9,25,49,81
'''
li = [1,2,3,4,5,6,7,8,9]
ans_li = [i*i for i in li if i % 2 == 1]
print(ans_li)
