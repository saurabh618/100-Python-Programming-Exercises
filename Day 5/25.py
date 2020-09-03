# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:04:42 2020

@author: saura
"""
'''
Question 25
    Define a class, which have a class parameter and have a same instance parameter.
'''
class MyClass():
    name = "rohan"
    def __init__(self, name=None):
        self.name = name
        
name = MyClass("saurabh")
print(name)
print(name.name)
print(MyClass.name)
print(MyClass)

name2 = MyClass()
name2.name = "Mohit"
print(name2)
print(name2.name)
print(MyClass.name)