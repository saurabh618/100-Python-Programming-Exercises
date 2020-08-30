# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:04:07 2020

@author: saura
"""
'''
# Question 2
> **_Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
> Then, the output should be:40320_**
'''
n = 8
fact = 1
i = 1
while i <= n:
    fact = fact * i;
    i = i + 1
print(fact)


def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(n))


from functools import reduce

def fun(acc, item):
	return acc*item

print(reduce(fun,range(1, n+1), 1))
