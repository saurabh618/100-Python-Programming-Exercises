# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 11:14:32 2020

@author: saura
"""
'''
Question 17
    Write a program that computes the net amount of a bank account based a transaction log from console input.
    The transaction log format is shown as following:
D 100
W 200
    D means deposit while W means withdrawal.
    Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
    Then, the output should be:
500
'''
total_D = 0
total_W = 0
data = input("Enter the transaction: ")

while True:
    if not data:
        break
    else:
        if data[0] == 'D':
            total_D += int(data[2:])
        elif data[0] == 'W':
            total_W += int(data[2:])    
    data = input()

print(total_D-total_W)

###########################################

# total = 0
# while True:
#     s = input().split()
#     if not s:            # break if the string is empty
#         break
#     cm,num = map(str,s)    # two inputs are distributed in cm and num in string data type

#     if cm=='D':
#         total+=int(num)
#     if cm=='W':
#         total-=int(num)

# print(total)

###########################################

# lst = []
# while True:
#   x = input()
#   if len(x)==0:
#     break
#   lst.append(x)

# balance = 0
# for item in lst:
#   if 'D' in item:
#     balance += int(item.strip('D '))
#   if 'W' in item:
#     balance -= int(item.strip('W '))
# print(balance)

###########################################

# transactions = []

# while True:
#     text = input("> ")
#     if text:
#     	text = text.strip('D ')
#     	text = text.replace('W ', '-')
#     	transactions.append(text)
#     else:
#         break	
# 		
# transactions = (int(i) for i in transactions)
# balance = sum(transactions)
# print(f"Balance is {balance}")
