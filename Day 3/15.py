# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:01:08 2020

@author: saura
"""
'''
Question 15
    Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
    Suppose the following input is supplied to the program:9
    Then, the output should be:11106
'''
input = 9
answer = input + (input*10+input) + (input*100+input*10+input) + (input*1000+input*100+input*10+input)
print(answer)

#########################

a = '9'
total,tmp = 0,str()        # initialing an integer and empty string

for i in range(4):
    tmp+=a               # concatenating 'a' to 'tmp'
    total+=int(tmp)      # converting string type to integer type

print(total)

#########################

from functools import reduce
print(reduce(lambda acc, a: int(acc) + int(a), [a*i for i in range(1,5)]))

#########################

total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total)
