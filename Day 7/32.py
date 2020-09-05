# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:27:00 2020

@author: saura
"""
'''
Question 32
Define a function which can generate a dictionary where the keys are numbers 
between 1 and 20 (both included) and the values are square of keys. 
The function should just print the keys only.
'''
def dict_func():
    my_dict = dict(enumerate((i*i for i in range(1,21)),1))
    print(my_dict.keys())
    
dict_func()
