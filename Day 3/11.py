# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 09:43:00 2020

@author: saura
"""
'''
Question 11
    Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
    and then check whether they are divisible by 5 or not. 
    The numbers that are divisible by 5 are to be printed in a comma separated sequence.
    Example:
0100,0011,1010,1001
    Then the output should be:
1010
'''
data = input("Enter four digit binary no.s: ").split(',')
output_li = []

for item in data:
    if int(item,2) % 5 == 0:
        output_li.append(item)
    
print(','.join(output_li))


data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))


data = list(filter(lambda i:int(i,2)%5==0, data))
print(",".join(data))
