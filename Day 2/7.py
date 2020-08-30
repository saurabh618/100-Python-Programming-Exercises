# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:54:46 2020

@author: saura
"""
'''
Question 7
    _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
    The element value in the i-th row and j-th column of the array should be i _ j.*
    Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
    Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
i,j = input("Enter two no.s, comma separated: ").split(sep=',')
i = int(i)
j = int(j)
li=[]

for row in range(i):
    temp_li = []
    for col in range(j):
        temp_li.append(col*row)
    li.append(temp_li)
print(li)


x,y = map(int,input().split(','))
lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)
