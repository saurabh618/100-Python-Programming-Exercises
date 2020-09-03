# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:44:43 2020

@author: saura
"""
'''
Question 22
    Write a program to compute the frequency of the words from the input. 
    The output should output after sorting the key alphanumerically.
    Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
input_str = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
li = input_str.split(" ")
my_set = set(li)
for item in sorted(my_set):
    print(f"{item}:{li.count(item)}")
