# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:42:15 2020

@author: saura
"""
'''
Question 14
    Write a program that accepts a sentence 
    and calculate the number of upper case letters and lower case letters.
    Suppose the following input is supplied to the program:
Hello world!
    Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
data = 'Hello World! How are you?'
count_lower = 0
count_upper = 0

for letter in data:
    if 'a' <= letter <='z':
        count_lower += 1
    elif 'A' <= letter <='Z':
        count_upper += 1

print(f'UPPER CASE {count_upper}')
print(f'LOWER CASE {count_lower}')

##############################################

upper = sum(1 for i in data if i.isupper())   # sum function cumulatively sum up 1's if the condition is True
lower = sum(1 for i in data if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))
