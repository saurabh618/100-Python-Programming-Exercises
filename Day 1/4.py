# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:15:47 2020

@author: saura
"""
'''
Question 4
Write a program which accepts a sequence of comma-separated numbers from console and 
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program: 34,67,55,33,12,98
    Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

'''
numbers = input("Enter comma separated numbers: ")
li = []
num = ''
for i in numbers:
    if i == ',':
        if num != '':
            li.append(num)
        num = ''
        continue
    elif i != ',' and i != ' ':
        num += i
if num != '':
    li.append(num)

print(li)
print(tuple(li))


li2 = numbers.split(sep = ',')
print(li2)
print(tuple(li2))
