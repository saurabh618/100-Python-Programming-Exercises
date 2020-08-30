# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 09:34:23 2020

@author: saura
"""
'''
Question 10
    Write a program that accepts a sequence of whitespace separated words as input 
    and prints the words after removing all duplicate words and sorting them alphanumerically.
    Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
    Then, the output should be:
again and hello makes perfect practice world
'''
message = input(" Enter message: ").split()
print(' '.join(sorted(set(message))))


for i in message:
    if message.count(i) > 1:  
        message.remove(i)

message.sort()
print(" ".join(message))
