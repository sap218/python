#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 11:14:33 2017

@author: sap21
"""

import math

# x is 200, make while loop until x is 99 | when x is less than len(python rules) | stop when sqrroot of 200

x = 200
while x is not 98:
    print(x)
    x = x - 1
print("above is x count down from 200 to 99")
print()

####

x = 200
string = "python rules the world"
print("length of string is", len(string))
while x is not (len(string) - 1):
    print(x)
    x = x - 1
print("above is x count down to length of string")
print()

####

x = 200
square_root = math.sqrt(200)
print(square_root)
while x is not square_root:
    print(x)
    x = x - 1
    if x < square_root:
        break
print("above is x count down to sqrt of 200")
