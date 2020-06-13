#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:48:27 2020

@author: ahmad
"""
#    0  1  2  3   4  5
x = [2, 6, 8, 9, -5, 6]

# write a code to print the sum of even numbers inside x
storage = 0
for i in range(len(x)):
    if x[i] % 2 == 0:
        storage += x[i]

print(storage)
print("/////////////////////////////")

# write a code to print the sum of odd numbers inside x
storage = 0
for i in range(len(x)):
    if x[i] % 2 != 0:
        storage += x[i]

print(storage)
print("/////////////////////////////")

# write a code to print the max number in x

print(max(x))

print("/////////////////////////////")

# write a code to print the max number in x

print(min(x))