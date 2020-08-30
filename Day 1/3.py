# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:08:49 2020

@author: saura
"""
'''
# Question 3
> **_With a given integral number n, write a program to generate a dictionary that contains 
(i, i x i) such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.Suppose the following input is
supplied to the program: 8,Then, the output should be:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}_**
'''

n = 8
ans = {}
for i in range (1,n+1):
    ans[i] = i * i
print(ans)


print({i : i*i for i in range(1,n+1)})


print(dict(enumerate((i * i for i in range(1,n+1)),1)))
