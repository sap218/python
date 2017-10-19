#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:00:11 2017

@author: sap21
"""
'''
#exercise 1
num1 = int(input('Enter a first number... '))
num2 = int(input('Enter a second number... '))
print(num1, " + ", num2, " = ", int(num1)+ int(num2))
print()

#exercise 2

#exercise 3
towns = []
for t in range(0,5):
    t = (input("enter a town in wales..."))
    towns.append(t)
print(sorted(towns))
print()
'''
#exercise 4
import random
dna = []
for c in range(0,100):
    c = random.choice(['A','C','G','T'])
    #dna.append(c.strip(","))
    dna.extend(', '.join(c))
print(dna)

#exercise 5
print()
string = [input("type in a sentence...")]
for i in string:
    string = i.split()
    new_string = i.split()
    if 'a' not in string and 'e' not in string and 'i' not in string and 'o' not in string and 'u' not in string:
        print(new_string)