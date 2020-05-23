#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:11:21 2020

@author: ahmad
"""

for i in range(0, 10):
    storage = ""
    for x in range(0, i + 1):
        storage += "*"
    print(storage)
    
# storage += "*"  => storage = storage + "*"
    
print("/////////////////////////")
for i in range(0, 10):
    storage = ""
    for x in range(0, 10):
        if x < 9 - i:
            storage += " "
        else:
            storage += "*"
    print(storage)
