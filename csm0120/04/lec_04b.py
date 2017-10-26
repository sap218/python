#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Oct 26 18:52:21 2017

@author: sap21
"""

print("#################")
print("ZeroDivisionError")
print("#################")

x = 5
y = 9 - (14 - x)
try:
    z = x / y
except ZeroDivisionError:
    z = 54
print(z)

print("##########")
print("IndexError") 
print("##########")

x = [3,7,5,2,9]
loc = 9
try:
    val = x[loc]
except IndexError:
    val = -1
print(val)

print()

x = [3,7,5,2,9]
loc = 9
try:
    val = x[loc]
except IndexError:
    print("Sorry, not enough samples in the data")
    print("There are only " + str(len(x)))
print(val)

print()
'''
import sys
y = [3,7,5,2,9]
exp = 9
try:
    value = y[exp]
except IndexError:
    print("Sorry, not enough samples in the data")
    print("There are only " + str(len(y)))
    sys.exit(1) # quitting the program
print(value)
'''
print()

x = [3,7,5,2,9]
loc = 9
try:
    val = x[loc]
except IndexError:
    print("Sorry, not enough samples in the data")
    print("There are only " + str(len(x)))
else: # continuing with else
    print(val)

print("##########")
print("ValueError")
print("##########")
'''
while True:
    try:
        n = int(input("Please enter a number: "))
        break
    except ValueError:
        print("That was not a valid number.")
        print("Please enter a number.")
print(n * 5)
'''
print("#######################################")
print("Generic Errors - exceptions vs. if-else")
print("#######################################")

#faster
'''
if len(forest_means) > 100:
    hundredth = forest_means[100]
else:
    hundredth = None
'''
#vs.
'''
try:
    hundredth = forest_means[100]
except IndexError:
    hundredth = None
'''
print()
'''
word = sys.stdin.readline().strip()
if isinstance(word,str) and word.isdigit() and len(word)<10:
    n = int(word)
else:
    n = None
'''
#vs.
'''
word = sys.stdin.readline().strip()
try:
    return int(word)
except (TypeError, ValueError, OverflowError): 
    return None    
'''    