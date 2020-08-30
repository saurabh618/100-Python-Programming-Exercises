# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:52:24 2020

@author: saura
"""
'''
# Question 1
> **_Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
> between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line._**
'''
li=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        li.append(str(i))

print (','.join(li))

print("\n")

for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
        
print("\n")


print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")

print("\n")


print(list(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")
