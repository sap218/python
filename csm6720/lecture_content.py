# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 13:17:05 2018

@author: sap21

>> Please note: this work isn't for my CS assignment.
>> All content was practice!
"""

import matplotlib.pyplot as plt

from pymongo import MongoClient
user = 'sap21'
dbpath = 'nosql.dcs.aber.ac.uk/sap21'
password = input('Enter Password...')
connection_string = 'mongodb://'+user+':'+password+'@'+dbpath
client = MongoClient(connection_string)
db = client.sap21

### Plot of records
'''
#plt.figure(1)
fig = plt.figure(1)
cursor = db.sap21.aggregate([{'$group':
    {'_id':'$vessel name', 'count':{'$sum':1}}}])
values = [x['count'] for x in cursor]
#print(values)
plt.hist(values)
plt.xlabel('Number of records for each ship')
plt.ylabel('Count of ships with N records')
plt.title('Distribution of number of records to each ship')
fig.savefig("test.png")
plt.show
'''
### Print out first record
from pprint import pprint
'''
cursor = db.sap21.find({})
for document in cursor[:1]:
    pprint(document)  
#doc = db.sap21.find_one({})
#pprint(doc)
'''
###

#vesselnamesu = db.sap21.distinct("vessel name")
#vesselnamesa = db.sap21.find_one("vessel name")
#print(vesselnames)
#for doc in vesselnames:
#    pprint(doc)
# 'Anne & Mary'
# 'Anne & Mary '
'''
cursoruno = db.sap21.find_one({"vessel name": "Anne & Mary"})
cursordos = db.sap21.find_one({"vessel name": "Anne & Mary "})
pprint(cursoruno)
pprint(cursordos)
'''
#idv = db.sap21.distinct("_id")
#print(idv)

# Edward Jones yob 1855 pob liverpool

'''
cursor = db.sap21.aggregate([{"$group": {"_id": {"mariners.name":"$mariners.name", "year_of_birth":"$year_of_birth"}}}])
#for row in cursor:
#    pprint(cursor)
people = [x for x in cursor]
pprint(people)
'''

cursor = db.sap21.aggregate([{"$unwind":"$mariners"},{"$group":{"_id":{"name":"$mariners.name","year_of_birth":"$mariners.year_of_birth"}}}])
for x in cursor:
    print(x)


'''
cursor = db.sap21.distinct("vessel name")
vessels = [x for x in cursor]
cursor = db.sap21.distinct("port of registry")
port = [x for x in cursor]
cursor = db.sap21.distinct("official number")
on = [x for x in cursor]
print(vessels, port, on)
'''
###
'''
print()
print()
cursor = db.sap21.distinct("mariners.name")
names = [x for x in cursor]
#name = []
#for i in names:
#       if i not in name:
#          name.append(i)
#name = list(set(name))
#len(names) != len(set(names)) # to check if duplicates

cursor = db.sap21.distinct("mariners.age").sort({"mariners.age":-1}) # desc
age = [x for x in cursor]
cursor = db.sap21.distinct("mariners.year_of_birth").count()
yob = [x for x in cursor]
cursor = db.sap21.distinct("mariners.place_of_birth")
pob = [x for x in cursor]
cursor = db.sap21.distinct("mariners.this_ship_capacity")
capacity = [x for x in cursor]

#for i in names:
#    print(names[i])
#    print(age[i])
print(names, age, yob, pob, capacity)
'''
###
'''
print()
cursor = db.sap21.distinct("mariners.name")
length = [x for x in cursor]
print(length)
'''
# https://stackoverflow.com/questions/11973725/how-to-efficiently-perform-distinct-with-multiple-keys
#cursor = db.sap21.aggregate([{"$group":{"_id":{'mariners.name':"$mariners.name", 'mariners.age':"$mariners.age"}}}]); #this
#cursor = db.sap21.aggregate([{"$group":{"_id":"$mariners", "entry":{ "$push":{ 'name':"$name", 'age':"$age"}}}}]).sort()
#mix = [x for x in cursor]
#print(mix)

# https://stackoverflow.com/questions/44256377/multiple-field-distinct-aggregation-in-mongodb
'''cursor = db.sap21.aggregate([
  { "$group": {
    "_id": "$mariners", # null
    "name": { "$addToSet": "$name" },
    "age": { "$addToSet": "$age" },
    "year_of_birth": { "$addToSet": "$year_of_birth" }
  }} 
])
values = [x for x in cursor]
print(values)
'''



'''
print()
cursor = db.sap21.distinct("mariners.name", {'mariners.age': {'$gte':60}}) # fuck yes this works
agegreaterthan = [x for x in cursor]
print(agegreaterthan)
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