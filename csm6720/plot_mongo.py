# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 13:17:05 2018

@author: sap21
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()
fig.savefig('test.png')
plt.show()

###

from pymongo import MongoClient
user = 'sap21'
dbpath = 'nosql.dcs.aber.ac.uk/sap21'
password = 'aX8eTY1f'
connection_string = 'mongodb://'+user+':'+password+'@'+dbpath
client = MongoClient(connection_string)
db = client.sap21

###
'''
plt.figure(1)
cursor = db.sap21.aggregate([{'$group':
    {'_id':'$vessel name', 'count':{'$sum':1}}}])
values = [x['count'] for x in cursor]
print(values)

plt.hist(values)
plt.xlabel('number of records for each ship')
plt.ylabel('count of ships with N records')
plt.title('Distribution of number of records to each ship')
plt.show
'''
###
'''
plt.figure(2)
cursor = db.sap21.aggregate([{'$group':
    {'_id':"$Mariner's name", '$age':{'$sum':1}}}]) # value
values = [x['value'] for x in cursor]
print(values)

plt.hist(values)
plt.show

###

plt.figure(3)
cursor = db.sap21.aggregate([{"$group":
    {"_id":"$mariner's name", "value":{"$avg":1}}}])
values = [x["value"] for x in cursor]
print(values)
plt.hist(values)
plt.show
'''
###

#cursor = db.sap21.aggregate([{
#    "$sortByCount":"mariner's name"}])
#print(cursor)
'''
cursor = db.sap21.aggregate([{"$group":
    {"_id": "$Mariner's name", "value":{"$max":5}}},
    {"$sort": {"value": -1}},
    {"$limit": 5}])
values = [x["value"] for x in cursor]
print(values)


cursor = db.sap21.aggregate([{"$group": {"_id":"$age", "count":{"$addToSet":1}}}])
values = str([x["count"] for x in cursor])
print(values)
'''

values = []
cursor = db.sap21.find({ "_id":"$vessel name", "$age":{"$lt":30} })
values = values.append(cursor)
print(values)

###

#db.sap21.find()[20:25]
cursor = db.sap21.find({"_id":"Mariner's name"})
print(cursor)
