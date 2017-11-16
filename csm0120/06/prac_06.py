#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:57:17 2017

@author: sap21
"""

import matplotlib.pyplot as plt

year = range(2002, 2013)
obesity = [1257, 1711, 2035, 2564, 3862, 5018, 7988, 10571, 11574, 11736, 10957]
female = [848, 1213, 1442, 1786, 2807, 3613, 5910, 8074, 8654, 8740, 8007]
male = [427, 498, 589, 746, 1047, 1405, 2077, 2495, 2919, 2993, 2950]

#plt.plot(year, obesity, 'c-', year, female, 'b-', year, male, 'r-')
plt.plot(year, obesity, 'LimeGreen', label='total')
plt.plot(year, male, 'MediumSlateBlue', label='male')
plt.plot(year, female, 'Orchid', label='female')
plt.ylabel('count')
plt.xlabel('year')
plt.title('obesity counts over years') #suptitle: above title
plt.legend()
plt.savefig("obesity.png") 