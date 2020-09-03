# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:08:22 2020

@author: saura
"""
'''
Question 30
Define a function that can accept two strings as input and print the string 
with maximum length in console. If two strings have the same length, 
then the function should print all strings line by line.
'''
def max_string(x,y):
    if len(x) > len(y):
        print(x)
    elif len(x) == len(y):
        print(x)
        print(y)
    else:
        print(y)
        
max_string("saurabh", "agarwal")

#########################################

func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)
func("hello","yoyoo")
