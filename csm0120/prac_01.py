# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:44:13 2017

@author: sap21
"""

myDNA = "ATTATTATTGC"
if myDNA.endswith("GC"):
    print("ends with GC", myDNA.count('T'), len(myDNA))

today = "Friday"
if today != "Saturday" and today != "Sunday":
    print("not the weekend")
else:
    print("weekend")
    
length = 20
width = 15
height = 48
volume = length * width * height
clothes = 14500
if volume < clothes:
    print("you need a bigger suitcase")
    
switch1 = 1
switch2 = 0
if switch1 == 1 and switch2 == 1:
    print("on")
else:
    print("off")
    
secret = 20
guess = 15
if guess > secret:
    print("too high")
elif guess < secret:
    print("too low")
elif guess == secret:
    print("correct")
    
date = 1
while date <= 31:
    if date == 1 or date == 8 or date == 15 or date == 22 or date == 29:
        print(date, "!")
    else:
        print(date)
    date = date + 1

###############################

print()

tt = 3 # 3 times table
mul = 1
while mul < 13:
    print(tt, "times", mul, "=", tt*mul)
    mul = mul + 1

print()

tt = 1 # whole times table
mul = 1
while tt < 12:
    while mul < 13:
        print(tt, "times", mul, "=", tt*mul)
        mul = mul + 1
    mul = 1
    tt = tt + 1
    while mul < 13:
        print(tt, "times", mul, "=", tt*mul)
        mul = mul + 1

print()

tt = 13 # whole times table in reverse
mul = 13
while tt > 1:
    while mul > 0:
        print(tt, "times", mul, "=", tt*mul)
        mul = mul - 1
    mul = 12
    tt = tt - 1
    while mul > 0:
        print(tt, "times", mul, "=", tt*mul)
        mul = mul - 1


