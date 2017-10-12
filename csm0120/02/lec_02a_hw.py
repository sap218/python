# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:00:52 2017

@author: samantha
"""

#write for loop print out even numbers between 50 and 100
for x in range(50,101,2):
        print (x)

#^^sum all even numbers and print sum at end, hint: make variable to collect sum
sum_even = 0
for x in range(50,101,2):
    print (x)
    sum_even = sum_even + x
print(sum_even)

#for loop print out leap years from now until 2500 (divisble by 4 except years divisible by 100 unless also visible by 400)
#2020
#print(list(range(2020,2501,4)))
for x in range(2017,2501):
    if x % 4 == 0:
        print(x)