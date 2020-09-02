# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:37:51 2020

@author: saura
"""
'''
Question 18
    A website requires the users to input username and password to register. 
    Write a program to check the validity of password input by users.
    Following are the criteria for checking the password:
        At least 1 letter between [a-z]
        At least 1 number between [0-9]
        At least 1 letter between [A-Z]
        At least 1 character from [$#@]
        Minimum length of transaction password: 6
        Maximum length of transaction password: 12
    Your program should accept a sequence of comma separated passwords and will check them 
    according to the above criteria. Passwords that match the criteria are to be printed, 
    each separated by a comma.
    Example
        If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345
        Then, the output of the program should be: ABd1234@1
'''
def lower_case(password):
    for i in password:
        if 'a' <= i <= 'z':
            return True
    return False

def number(password):
    for i in password:
        if i in '0123456789':
            return True
    return False

def upper_case(password):
    for i in password:
        if 'A' <= i <= 'Z':
            return True
    return False

def special_char(password):
    for i in password:
        if i in ['$','#','@']:
            return True
    return False

def length(password):
    if 6 <= len(password) <=12:
        return True
    return False
   
password = 'ABd1234@1,a F1#,2w3E*,2We3345,sauRabh90@'
li_password = password.split(',')

for pw in li_password:
    if lower_case(pw) and number(pw) and upper_case(pw) and special_char(pw) and length(pw):
        print(pw, end = ',')
    