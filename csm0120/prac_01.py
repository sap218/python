#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 10:19:37 2017

@author: sap21
"""

#redoing practical 1

#exercise 1
dna = "ATTATTATTGC"
if dna.endswith("GC"):
    print("has a sticky end")
print(dna.count('T'))
print(len(dna))

print("###################################")
    
#exercise 2
today = "Friday"
if today == "Saturday" or today == "Sunday":
    print("weekend")
else:
    print("not weekend")
    
print("###################################")

#exercise 3
length = 20
width = 15
height = 48
volume = length * width * height
clothes = 14500
if volume < clothes:
    print("suitcase too small for clothes")
    
print("###################################")

#exercise 4
switch1 = 1
switch2 = 0
if switch1 == 1 and switch2 == 1:
    print("on")
else:
    print("off")
    
print("###################################")

#exercise 5
secret = 20
guess = 15
if guess < secret:
    print("guess too low")
elif guess > secret:
    print("guess too high")
elif guess == secret:
    print("guess correct")
    
print("###################################")

#exercise 6
for x in range(1,32):
    if x == 1 or x == 8 or x == 15 or x == 22 or x == 29:
        print(x, "!")
    else:
        print(x)
        
print("###################################")

#exercise 7
multiply = 3
for x in range(1,13):
    print("3 times ", x, " = ", x * multiply)
    
print("###################################")

#exercise 8
t = 1
while t < 12:
    t = t + 1
    mul = 1
    while mul < 13:
        print(mul, " times ", t, " = ", mul * t)
        mul = mul + 1
        
print("###################################")
        
#exercise 9

t = 13
while t > 1:
    t = t - 1
    mul = 12
    while mul > 1:
        print(mul, " times ", t, " = ", mul * t)
        mul = mul - 1