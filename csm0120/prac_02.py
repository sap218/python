#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:27:43 2017

@author: sap21
"""

#redoing practical 2

#exercise 1
num1 = input("enter num1: ")
num2 = input("enter num2: ")
print("num1 + num2 = ", int(num1) + int(num2))

print("###################################")
   
#exercise 2
multiply = 3
for x in range(1,13):
    print("3 times ", x, " = ", x * multiply)
print()
for t in range(1,13):
    for mul in range(1,13):
        print(mul, " times ", t, " = ", mul * t)
print()
for t in range(12,0,-1):
    for mul in range(12,0,-1):
        print(mul, " times ", t, " = ", mul * t)

print("###################################")   

#exercise 3
towns = []
for t in range(0,5):
    t = (input("enter town..."))
    towns.append(t) 
print(towns)
print(sorted(towns))

print("###################################")
        
#exercise 4
import random
dna = []
for c in range(0,101):
    c = random.choice(['A','C','G','T'])
    dna.append(c)
print("".join(dna))

print("###################################")

#exercise 5
string = input("enter a sentence:")
vowels = ["a", "e", "i", "o", "u"]
sentence = []
for v in string:
    if v not in vowels:
        #print(v)
        sentence.append(v)
print("".join(sentence))

print("###################################")

#exercise 6
import random
letters = []
for num in range(65,91):
    letters.append(chr(num))
rlist = random.sample(letters, 10)
#print(letters)
print("here are the random letters: ", rlist)
acceptable = False
while not acceptable:
    acceptable = True
    word = input("input a word from the random letters...")
    
    if len(word) < 3:
        print("too short")
        acceptable = False
    
    for l in word:
        if l not in rlist:
            acceptable = False
    
    if acceptable:
        print("word accepted")
    else:
        print("word not accepted")

print("###################################")
        
#exercise 7
import random
forests = []
means = []
for f in range(1001):
    trees = []
    for t in range(101):
        t = random.uniform(0.5,5)
        trees.append(t)
    forests.append(trees)
    mean = sum(trees) / 100
    means.append(mean)
#print("means: ", sorted(means))
s_means = sorted(means)
print(s_means[:50])
amazon = 2.5
if amazon <= s_means[50]:
    print("within bottom 5%")
else:
    print("greater than 5%")