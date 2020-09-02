# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:01:26 2020

@author: saura
"""
'''
Question 19
You are required to write a program to sort the (name, age, score) tuples by ascending order 
where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
    1: Sort based on name
    2: Then sort based on age
    3: Then sort by score
    The priority is that name > age > score.
    If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
    Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''
data = input("Enter name,age,score: ")
li_data = []
my_list = []

while True:
    if not data:
        break
    li_data.append(data)
    data = input()

for item in li_data:
    my_tuple = ()
    individual_data = item.split(',')
    name = individual_data[0]
    age = individual_data[1]
    score = individual_data[2]
    my_tuple = (name,age,score)
    my_list.append(my_tuple)

print(sorted(my_list))

###################################

lst = []
while True:
    s = input().split(',')
    if not s[0]:
        break
    lst.append(tuple(s))

lst.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))  
# here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order

print(lst)

'''
above is similar to the below example.

a = [(0,2),(4,4),(10,-1),(5,3)]
a.sort(key=lambda x:x[1], reverse=False)
print(a)
'''