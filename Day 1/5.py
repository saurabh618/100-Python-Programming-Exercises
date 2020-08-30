# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 14:54:30 2020

@author: saura
"""
'''
Question 5
    Define a class which has at least two methods:
        getString: to get a string from console input
        printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
'''
class MyClass():
    
    def getString(self):
        self.string = input("Enter a string: ")
        
    def printString(self):
        print(self.string.upper())

my_obj = MyClass()
my_obj.getString()
my_obj.printString()
