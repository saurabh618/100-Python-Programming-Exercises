# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:55:46 2020

@author: saura
"""
'''
Question 20
    Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''
class GenClass():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def gen_method(self):
        for i in range(self.num1, self.num2 + 1):
            if i % 7 == 0:
                yield i

range_num = GenClass(0,100)
for item in range_num.gen_method():
    print(item)
    
############################################
    
class MyGen():
    def by_seven(self, n):
        for i in range(0, int(n/7) + 1):
            yield i * 7

for i in MyGen().by_seven(100):
    print(i)
    
