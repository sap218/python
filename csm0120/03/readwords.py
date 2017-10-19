#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:11:58 2017

@author: sap21
"""

myfile = open("words.txt")
#print(myfile) #prints info
for line in myfile:
    print(line.strip())
myfile.close()
'''
myfile = open("words.txt")
for line in myfile.readlines(): #readlines returns items as a list
    print(line)
myfile.close()
'''

''' #while loop
myfile = open("words.txt")
line = myfile.readline()
while line:
    print(line.strip())
    line = myfile.readline()
myfile.close()
'''
print()

myfile = open("words.txt")
for line in myfile:
    if line.startswith('a'):
        print(line)
myfile.close()

print() ############### split provides list which can be saved as a variable
print() ############### strip also removes white space, etc

uni_file = open("modules.txt")
for line in uni_file:
    module = (line.split(","))
    #print(len(module))
    if len(module) != 4:
        print(module)
uni_file.close()

print()
print() # CSV: lines separated by commas
print()

import csv
my_csv = open("modules.csv")
csvreader = csv.reader(my_csv, dialect='excel')
for line in csvreader:
    print("entry: ", line) # each line is a list 
    print("mod_code: ", line[0]) # 0 element
    print("title: ", line[1])
    print("length: ", len(line))
    print()
my_csv.close()

# counts how many modules taught in semester 1
# only prints out module codes that Neil Taylor runs