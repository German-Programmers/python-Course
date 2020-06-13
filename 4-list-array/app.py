#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:10:10 2020

@author: ahmad
"""

x = [2, 6, 8, 9, -5, 6]
c = ["cat", "dog", "elephant"]

print(x[4])

print(len(c))

print("////////////////////////")

for i in range(0, len(x) ):
    print(x[i])

print("////////////////////////")
    
print(*x, sep = " - ")

print("////////////////////////")

# first way
#total = sum(x) 
#print(total)

#secodn way
total = 0

for i in range(len(x)):
    total += x[i]
    
print(total)