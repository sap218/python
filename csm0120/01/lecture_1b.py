#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 10:10:51 2017

@author: sap21
"""
#note strings are sorted alphabetically

import math

print(math.exp(3))
print(math.log2(64)) #2 is base | math.log(64, 2)

#pi*r^2
r = 6
print((math.pi)*(r**2))
r *= r
print(r)

##

x = "apples"
y = 6/4
print(x)
print(y)
print(x + str(y)) #y must be a string

print("a" * 3)

print(int(True), int(False)) #float works too

##

paragraph = """string multiplle prints
here - etc"""
print(paragraph, len(paragraph))

##

seq = "ATGCTTATACA"
print(seq, seq.count("A"), seq.startswith("AT"), seq.endswith("GC"), seq.find("G"), seq.find("N"))

a = "a,b,c,d,e,,,,"
print(a, a.strip(","))

b = "2,3,5,y,n,large"
print(b, b.split(","))

###

x = "hello and welcome to python"
split_x = x.split()
new_x = ",".join(split_x)
print(x, split_x, new_x)

x = ["1","2","3","4"]
spaced_x = " ".join(x)
tabbed_x = "\t".join(x)
csv_x = ",".join(x)
woo_x    = "woo".join(x)

##

temp = 5 * math.sin(2.5)
rain = 3
if temp < 3:
    print("CHILLY")
    if rain == 5:
        print("UMBERLLA")
    else:
        print("YOU GOOD")
elif temp < 10:
    print("Feeling cold! Only " + str(temp))
    print("wear trousers")
else:
    print("We're enjoying summer")
    print("wear shorts")
    
##

c = 0
while c < 10:
    print("Hello world " + str(c)) 
    c = c + 1
