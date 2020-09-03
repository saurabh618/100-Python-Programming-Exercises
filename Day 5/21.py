# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:23:20 2020

@author: saura
"""
'''
Question 21
    A robot moves in a plane starting from the original point (0,0). 
    The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
    The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
    The numbers after the direction are steps. Please write a program to 
    compute the distance from current position after a sequence of movement 
    and original point. If the distance is a float, then just print the 
    nearest integer. Example: If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
    Then, the output of the program should be: 2
'''
import math
direction = (5,3,3,2)  # up, down, left, right
initial_pos = (0,0)
final_pos = (direction[0] - direction[1], - direction[2] + direction[3])
distance = math.sqrt(((final_pos[0] - initial_pos[0]) ** 2) + ((final_pos[1] - initial_pos[1]) ** 2))
print(distance)
