#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:08:23 2017

@author: sap21
"""

'''
location = {
        "Aber": (52.4, -4.1),
        "Cardiff": (51.4, -3.1),
        "Edinburgh": (55.9, -3.2)
}
for town in location:     # .keys() is default
    print(town)
    for (lat, lon) in location.values():
        if lon < 0:
            print("West")
        else:
            print("East")
'''

# a string can be used as a list of characters 
my_list = "hello world" # my_list.find("h")
my_dict = {}
for c in my_list: # loop through items in list and add to dictionary
    my_dict[c] = 1
for k in my_dict: #dictionary is filled, lets see what keys we have
    print(k)
print()    
    
numbers = [3,5,6,7,8,4,5,7,6,7,9,2]
unique_dict = {}
for num in numbers:
    unique_dict[num] = 1
for num in unique_dict: # sorted(unique_dict.keys()) to sort
    print(num)
print()
    
friends_dictionary = {}
friends_dictionary['sap21'] = 'Sam'
friends_dictionary['avr1'] = 'Amy'
friends_dictionary['kis12'] = 'Kieran'
friends_dictionary['jas111'] = 'James'
print(friends_dictionary)
print()
print("keys: ", list(friends_dictionary.keys()))
print("values: ", list(friends_dictionary.values()))
print("items: ", list(friends_dictionary.items()))
print()
for k in friends_dictionary.keys():
    print(friends_dictionary[k])
print()
my_key = "bbr3"
if my_key in friends_dictionary:
    print(friends_dictionary[my_key])
else:
    print(my_key + " is not there")
print()

person = "sap21"
if person  in friends_dictionary:
    print(person + " is in dictionary: " + friends_dictionary["sap21"])
else:
    print(person + " not found")
print()    
##################
##################
'''
import sys # good for plain terminals: python console (not IPython)
print("Please enter your name")
name = sys.stdin.readline().strip()
# or
name = input("Please enter your name\n") # don't use if runs on Python2
'''
#################
#################
'''
import sys
user_dict = {}

for i in range(0,4):
    print("Please enter your name")
    name = sys.stdin.readline().strip()

    print("Please enter your username")
    user_name = sys.stdin.readline().strip()

    user_dict[user_name] = name
    print(user_dict)
print(user_dict)

print(user_dict['sap21'])
print(user_dict.get('sap21'))
# print(my_dict.get('d', 0))
'''
#################
#################

colours = set()
colours = {"red","green","blue"}
colours.add("purple")
print(colours)
print()
#"red" in colours
# chars = set("hello world")

#################

x = {1, 2, 3}
y = {3, 4, 5}
print(x, y) # union and intersection
print(x | y)
print(x & y)

#################

print()
total = 3.477777777
item = "apples"
print("Total for " + item + " is: " + str(total))
print("Total for {} is: {}".format(item, total))
print("Total for %s is: %f" % (item, total))
print("Total for {0} is: {1:.2f}".format(item, total))
print()
print("%d is for integers" % (8))
print("%f is for floats" % (3.1412))
print("%s is for strings" % ("apples"))
print("%% prints a percentage sign" % ())