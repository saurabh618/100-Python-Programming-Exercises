# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:04:05 2020

@author: saura
"""
'''
Question 6
    Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.
    For example Let us assume the following comma separated input sequence is given to the program:100,150,180
    The output of the program should be: 18,22,24
'''

num = input("Enter comma separated numbers: ").split(sep = ',')
c = 50
h = 30
li = []
for d in num:
    q = ((2*c*int(d))/h) ** (0.5)
    li.append(str(round(q)))
print(','.join(li))


print(','.join(list(map(lambda d:str(round(((2*c*int(d))/h)**(0.5))), num))))
#print(','.join(list(map(lambda d:str(round(((2*c*int(d))/h)**(0.5))), input().split(sep=',')))))


print(*(round((2*c*int(d)/h)**0.5) for d in num), sep=",")

