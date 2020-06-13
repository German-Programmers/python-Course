#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 17:24:07 2020

@author: ahmad
"""




def sayHello():
    print("hello1")
    print("Hello again")


def welcome(name):
    print("Hello " + name)
    
welcome("Ahmad")
welcome("Ali")

# write a function to print numbers from 0 to n

def counter(n):
    for i in range(0, n+1):
        print(i)
        
counter(10)
print("////////////////////////")

def joiner(firstName, lastName):
    print(firstName + " " + lastName)
    
joiner("Ahmad", "Osman")

print("////////////////////////")
def sum(num1, num2):
    return num1 + num2

result = sum(5, 6)
print(result)

# write a function to return the sum of a given numbers list
print("////////////////////////")
def arrSum(arr):
    storage = 0
    for i in arr:
        storage += i
    return storage

print(arrSum([5, 2, 3, 9, 6]))



























