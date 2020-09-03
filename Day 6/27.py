# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:59:58 2020

@author: saura
"""
'''
Question 27
Define a function that can convert a integer into a string and print it in console.
'''
def int_to_str(item):
    print(str(item))
    
int_to_str(45)

###########################################

conversion = lambda x:str(x)
print(conversion)
print(type(conversion))
print(conversion(56))
print(type(conversion(56)))