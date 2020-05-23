#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:49:24 2020

@author: ahmad
"""

x = [5, 9, 8, -8, 7, 8, 10]
#print(x[4])

#for i in range(0,len(x)):
#    print(x[i])

# write a code to show the sum og the numbers in the Array
sum = 0
for i in range(0,len(x)):
    sum += x[i]

print("array sum = " + str(sum))

# write a code to print the max number in the array

max = x[0]

for i in range(1, len(x)):
    if max < x[i]:
        max = x[i]

print("array max = " + str(max))
 


    


