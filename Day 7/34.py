# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 11:04:52 2020

@author: saura
"""
'''
Question 34
Define a function which can generate a list where the values are square of 
numbers between 1 and 20 (both included). Then the function needs to print 
the first 5 elements in the list.
'''
def sq_func(elements):
    li = [i**2 for i in range(1,21)]
    print(li[0:elements])


sq_func(5)
