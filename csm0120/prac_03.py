#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:14:21 2017

@author: sap21
"""

#redoing practical 3

#exercise 1
'''
grades = {}
entries = input("entries...")
for g in range(int(entries)): #range(0,5)
    uid = input("enter student uid...")
    per = input("enter student percentage...")
    while int(per) < 0 or int(per) > 100:
        print("incorrect grade")
        per = input("enter student percentage...")
    grades[uid] = int(per)
print(grades)
total = sum(grades.values())
mean = total / 5
print(mean)
print("###################################")
print()
for uid in sorted(grades.keys()):
    print(uid, "\t", grades[uid]) #\t table

print()
ins = ""

#while ins in grades:
while ins != "stop":
    ins = input("enter uid...")
    if ins not in grades:
        print("not in system")
    else:
        print(grades[ins])
'''
print("######################################################################")

#exercise 2

def happy_birthday(age):
    if age >= 100:
        print("HB from Queen!")
    elif age > 20 and age < 100:
        print("another year older")
    elif age <= 20:
        print("congrats you are", age, "years old")
        
print("######################################################################")        
        
#exercise 3

import random
def generate():
    dna = []
    for c in range(0,101):
        c = random.choice(['A','C','G','T'])
        dna.append(c)
    return "".join(dna)

dna = generate()
print(dna)

def compliment(dna):
    dna_base = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    compliment = []
    for base in dna:
        base = dna_base[base]
        compliment.append(base)
    return "".join(compliment)

print("|" * len(dna)) #exercise.4
print(compliment(dna))
    
print("######################################################################")
    
#exercise 4

print("######################################################################")
    
#exercise 5

