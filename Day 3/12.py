# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 10:05:43 2020

@author: saura
"""
'''
Question 12
    Write a program, which will find all such numbers between 1000 and 3000 (both included) 
    such that each digit of the number is an even number.The numbers obtained should be printed 
    in a comma-separated sequence on a single line.
'''
num_li = list(range(1000,3001))
out_li = []

for num in num_li:
    check = 0
    for individual_num in str(num):
        if int(individual_num) % 2 == 0:
            check += 1
    if check == len(str(num)):
        out_li.append(str(num))

print(','.join(out_li))


def check(element):
    return all(int(i) % 2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]
lst = list(filter(check,lst))
print(",".join(lst))