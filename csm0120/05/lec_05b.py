#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:31:06 2017

@author: sap21
"""

# http://matplotlib.org/

import matplotlib.pyplot as plt





#################
'''line graphs'''
#################

# simple plot
plt.plot([1, 3, 2, 4]) # plot against y
plt.show()

#########
#changing plot and adding axis

plt.plot([10, 20, 30, 40], [1, 10, 2, 7], 'k:')
plt.ylabel('some y axis')
plt.xlabel('some x axis')
plt.show()

# c- = changed colour
# scatter: bv = triangles, ro = round, g. = small round, k: = dotted

#########
# multiple of same but with different plot type

x = [10, 20, 30, 40]
y = [1, 3, 2, 4]
plt.plot(x, y,'bv', x, y, 'b-')
plt.ylabel('y axis')
plt.xlabel('x axis')
plt.show()

#########
# two different plots on same graph

x  = [10, 20, 30, 40]
y1 = [1, 3, 2, 4]
y2 = [1.5, 2.5, 3.5, 4.5]
plt.plot(x, y1, 'b-', x, y2, 'r-')
plt.axis([0, 50, 0, 5])
plt.ylabel('y')
plt.xlabel('x')
plt.show()

#########
# someting about axis - see comment

x = [10, 20, 30, 40]
y = [1, 3, 2, 4]
plt.plot(x, y, 'bv', x, y, 'b-')
plt.axis([0, 50, 0, 5]) # axis
plt.ylabel('the y')
plt.xlabel('some x')
plt.show()






################
'''bar charts'''
################

#simple bar chart
x     = [1, 2, 3, 4]
mouse = [10, 12, 20, 15]
plt.bar(x, mouse)
plt.xticks(x, ('A', 'T', 'C', 'G')) # labelling x-axis
plt.show()

#########

x     = [1, 2, 3, 4]
mouse = [10, 12, 20, 15]

barwidth = 0.8
midpoints = []
for b in x:
    midpoints.append(b + barwidth/2)
    
plt.bar(x, mouse, barwidth)
plt.xticks(midpoints, ('A', 'T', 'C', 'G'))
plt.show()

#########
# two bar charts

x     = [1, 2, 3, 4]
mouse = [10, 12, 20, 15]
human = [11, 14, 5, 5]
barwidth = 0.4
midpoints = []
for b in x:
    midpoints.append(b + barwidth)
plt.bar(x, mouse, barwidth, color='r')
plt.bar(midpoints, human, barwidth, color='b')
plt.xticks(midpoints, ('A', 'T', 'C', 'G'))
plt.show()

######### 
# legend

x     = [1, 2, 3, 4]
mouse = [10, 12, 20, 15]
human = [11, 14, 5, 5]
barwidth = 0.4
midpoints = []
for b in x:
    midpoints.append(b + barwidth)
plt.bar(x, mouse, barwidth, color='r', label='mouse')
plt.bar(midpoints, human, barwidth, color='b', label='human')
plt.xticks(midpoints, ('A', 'T', 'C', 'G'))
plt.legend()
plt.show()

#########
# adding grid

x     = [1, 2, 3, 4]
mouse = [10, 12, 20, 15]
human = [11, 14, 5, 5]
barwidth = 0.4
midpoints = []
for b in x:
    midpoints.append(b + barwidth)
plt.bar(x, mouse, barwidth, color='r', label='mouse')
plt.bar(midpoints, human, barwidth, color='b', label='human')
plt.xticks(midpoints, ('A', 'T', 'C', 'G'))
plt.legend()
plt.grid(True, axis = 'y')
plt.show()

#########

'''
Read the documentation for scatter plots: http://matplotlib.org/api/pyplot_api.html?highlight=scatter#matplotlib.pyplot.scatter
Produce a scatter plot with green diamond markers for the following data
import random
x = range(0,100)
y = random.sample(range(1000),100) 
'''



#########
# returning to scatter
# error bar

x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 22, 28]
errors = [2.2, 1.5, 1.8, 2.8, 1.4]
plt.errorbar(x, y, yerr=errors)
plt.axis([0, 6, 0, 40])
plt.ylabel('the y axis name')
plt.xlabel('some x axis')
plt.show()

#########
# error bar by themselves

x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 22, 28]
errors = [2.2, 1.5, 1.8, 2.8, 1.4]
plt.errorbar(x, y, yerr=errors, fmt="none")
plt.axis([0, 6, 0, 40])
plt.ylabel('the y axis name')
plt.xlabel('some x axis')
plt.show()

#########
# error bars (w/ colour) and plot

x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 22, 28]
errors = [2.2, 1.5, 1.8, 2.8, 1.4]
plt.plot(x, y, 'b-', x, y, 'bo')
plt.errorbar(x, y, yerr=errors, fmt="none", ecolor="r") # error bar colour
plt.axis([0, 6, 0, 40])
plt.ylabel('the y axis name')
plt.xlabel('some x axis')
plt.show()

#########
#saving image
'''
plt.ioff() # shows figure & saves
x     = [1, 2, 3, 4]
mouse = [10, 12, 20, 15]
plt.bar(x, mouse)
plt.savefig("fig.png", dpi=200) # resolution
plt.savefig("fig.pdf")
plt.savefig("fig.tiff")
# plt.show()
'''






###############
'''date time'''
###############

import datetime
dt = datetime.datetime(2017,11,5)  
print(dt.weekday()) # 0 = Monday, etc... 6 = Sunday
'''
datetime.time
datetime.datetime
datetime.timedelta
datetime.tzinfo
''' #https://docs.python.org/3/library/datetime.html
#########

import datetime as dt
x = "2015-01-25 11:33 AM GMT"
# We need to describe the format of the string
format = "%Y-%m-%d %I:%M %p %Z"
mydt = dt.datetime.strptime(x, format)

#########
# plotting with dates
'''
# so you have a list of datetimes
plt.plot(dts, y, 'ro', dts, y, 'r-')
# Will tilt the date labels on the x axis
plt.gcf().autofmt_xdate()
'''
#########
'''
You're given a file called tides.csv
This contains predictions about high tides and low tides in December 2014 and January 2015.
Read in the file and plot the tide heights of high tides against the datetimes of the high tides.
Make decisions about the x-axis. What would you like to use? 
Plot the tide heights of low tides on the same figure. 
'''
#########
#########