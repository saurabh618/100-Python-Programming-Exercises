# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:06:54 2020

@author: saura
"""
'''
Question 13
    Write a program that accepts a sentence and calculate the number of letters and digits.
    Suppose the following input is supplied to the program:
hello world! 123
    Then, the output should be:
LETTERS 10
DIGITS 3
'''
message = "hello world! 123"

num = '0123456789'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet + alphabet.upper()

count_num = 0
count_alpha = 0

for item in message:
    for number in num:
        if number == item:
            count_num += 1
            break
        
    for letter in alphabet:
        if letter == item:
            count_alpha += 1
            break

print(f"Letters: {count_alpha}")
print(f"Digits: {count_num}")

#######################################################

word = "hello world! 123"
letter,digit = 0,0

for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i<='9':
        digit+=1

print("LETTERS {0}\nDIGITS {1}".format(letter,digit))

########################################################

letter, digit = 0,0

for i in word:
    if i.isalpha(): # returns True if alphabet
        letter += 1
    elif i.isnumeric(): # returns True if numeric
        digit += 1
print(f"LETTERS {letter}\nDIGITS {digit}")

########################################################

import re
counter = {"LETTERS":len(re.findall("[a-zA-Z]", word)), "NUMBERS":len(re.findall("[0-9]", word))}
print(counter)

