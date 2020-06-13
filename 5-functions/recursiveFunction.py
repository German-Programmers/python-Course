#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:02:10 2020

@author: ahmad
"""

#def recursive():
#    print("hi")
#    recursive()
#
#
#recursive()

def factor(n):
    if (n == 1):
        return 1
    return n * factor(n-1)
 
print(factor(5))
    