#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:15:15 2020

@author: ahmad
"""
# write a function to calculate the factor of the number
# example user enter 5
# 5 *4 * 3 * 2 * 1
# check the input is a positive number and

#solution
x = 5
storag = 1
for n in range(2 , x+1):
    storag = storag * n
    
print(storag)

# calculate the sum of even number from 1 to 100
#solution
sum = 0
for c in range(2, 101, 2):
    sum = sum + c

print(sum)
 
