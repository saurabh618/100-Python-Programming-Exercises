# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:19:03 2020

@author: saura
"""
'''
Question 8
    Write a program that accepts a comma separated sequence of words as input and prints the words in a 
    comma-separated sequence after sorting them alphabetically.
    Suppose the following input is supplied to the program:
without,hello,bag,world
    Then, the output should be:
bag,hello,without,world

'''
li = input().split(',')
li.sort()
print(*(li),sep=',')


print(','.join(li))
