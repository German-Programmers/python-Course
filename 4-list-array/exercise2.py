#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:19:19 2020

@author: ahmad
"""

x = [4, 5, -2, 3, 5]
#x.reverse()
for i in range(len(x) - 1, -1, -1 ):
    print(x[i])
    
# write a code to order x desc

print("//////////////////")

for f in range(0, len(x)):
    min = x[0]
    for i in x:
        if (min < i):
            min = i
        
    print(min)
    x.remove(min)
    
    
    
    