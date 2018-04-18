# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 13:17:05 2018

@author: sap21
"""

import matplotlib.pyplot as plt

from pymongo import MongoClient
user = 'sap21'
dbpath = 'nosql.dcs.aber.ac.uk/sap21'
password = input('Enter Password...')
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
plt.xlabel('Number of records for each ship')
plt.ylabel('Count of ships with N records')
plt.title('Distribution of number of records to each ship')
plt.show
'''
###

print()
cursor = db.sap21.distinct("vessel name")
vessels = [x for x in cursor]
cursor = db.sap21.distinct("port of registry")
port = [x for x in cursor]
cursor = db.sap21.distinct("official number")
on = [x for x in cursor]
print(vessels, port, on)

###

print()
print()
cursor = db.sap21.distinct("mariners.name")
names = [x for x in cursor]
name = []
for i in names:
       if i not in name:
          name.append(i)
name = list(set(name))
#len(names) != len(set(names)) # to check if duplicates

cursor = db.sap21.distinct("mariners.age")
age = [x for x in cursor]
cursor = db.sap21.distinct("mariners.year_of_birth")
yob = [x for x in cursor]
cursor = db.sap21.distinct("mariners.place_of_birth")
pob = [x for x in cursor]
cursor = db.sap21.distinct("mariners.this_ship_capacity")
capacity = [x for x in cursor]

'''for i in names:
    print(names[i])
    print(age[i])'''
print(name, age, yob, pob, capacity)






















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
'''
values = []
cursor = db.sap21.find({ "_id":"$vessel name", "$age":{"$lt":30} })
values = values.append(cursor)
print(values)

###

#db.sap21.find()[20:25]
cursor = db.sap21.find({"_id":"Mariner's name"})
print(cursor)
'''