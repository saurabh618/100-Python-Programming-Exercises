# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:15:44 2020

@author: saura
"""
'''
Question 31
Define a function which can print a dictionary where the keys are numbers 
between 1 and 20 (both included) and the values are square of keys.
'''
def sq_dict():
    return {i:i*i for i in range(1,21)}

print(sq_dict())

#####################################

print(dict(enumerate((i * i for i in range(1,21)),1)))
