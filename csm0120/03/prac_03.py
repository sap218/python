#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:04:44 2017

@author: sap21
"""

# exercise 1

grades = {}
total_students = input("total entries...")

for g in range(0,(int(total_students))):
    name = input("enter student name...")
    percent = input("enter student grade...")
    while int(percent) < 0:
        percent = input("percentage incorrect, please enter a new one...")
    while int(percent) > 100:
        percent = input("percentage incorrect, please enter a new one...")
    grades[name] = int(percent)
print()
print(grades)
print()
print("sum of all grades: ", sum(grades.values()))
mean_grades = (sum(grades.values()))/(int(total_students))
print("mean of grades: ", mean_grades)
print()
stu_keys = list(grades.keys())
stu_val = list(grades.values())
print(stu_keys, stu_val)

'''s = 0
for s in grades:
    print(grades.keys())
    s = int(s) + 1
  '''  
    
# exercise 2
'''
def happy_birthday(age):
    if age > 100:
        print("HB from Queen!")
    elif age > 20 and age < 100:
        print("another year older")
    elif age < 20:
        print("congrats you are ", age, "years old")
'''