# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 11:02:39 2020

@author: saura
"""
'''
Question 33
Define a function which can generate and print a list where the values are 
square of numbers between 1 and 20 (both included).
'''

def sq_func():
    li = [i**2 for i in range(1,21)]
    print(li)
    
sq_func()
