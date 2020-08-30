# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:27:52 2020

@author: saura
"""
'''
Question 9
    Write a program that accepts sequence of lines as input and prints the lines after 
    making all characters in the sentence capitalized.
    Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
    Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

string = input("Enter paragraph: ") + "\n"
while True:
    new_string = input()
    string += new_string + "\n"
    if new_string == '':
        break 

print(string.upper())

#############################################

def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s

my_list = []
for line in map(str.upper, user_input()):
    my_list.append(line)

for line in my_list:
    print(line)
