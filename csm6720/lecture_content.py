# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 13:17:05 2018

@author: sap21

>> Please note: this work isn't for my CS assignment.
>> All content was practice!
"""

import matplotlib.pyplot as plt
from pprint import pprint
from pymongo import MongoClient
user = 'sap21'
dbpath = 'nosql.dcs.aber.ac.uk/sap21'
password = input('Enter Password...')
connection_string = 'mongodb://'+user+':'+password+'@'+dbpath
client = MongoClient(connection_string)
db = client.sap21

### Plot of records
plt.figure(1)
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

### Print out first record
cursor = db.sap21.find({})
for document in cursor[:1]:
    pprint(document)  
    
### Print out vessel information
cursor = db.sap21.distinct("vessel name")
vessels = [x for x in cursor]
cursor = db.sap21.distinct("port of registry")
port = [x for x in cursor]
cursor = db.sap21.distinct("official number")
on = [x for x in cursor]
print(vessels, port, on)

### Print out Mariner Information
cursor = db.sap21.distinct("mariners.name")
names = [x for x in cursor]
#len(names) != len(set(names)) # to check if duplicates - but not needed since used distinct

cursor = db.sap21.distinct("mariners.age").sort({"mariners.age":-1}) # desc
age = [x for x in cursor]
cursor = db.sap21.distinct("mariners.year_of_birth").count()
yob = [x for x in cursor]
cursor = db.sap21.distinct("mariners.place_of_birth")
pob = [x for x in cursor]
cursor = db.sap21.distinct("mariners.this_ship_capacity")
capacity = [x for x in cursor]

for i in names:
    print(names[i])
    print(age[i])
print(names, age, yob, pob, capacity)

cursor = db.sap21.distinct("mariners.name", {'mariners.age': {'$gte':60}}) # this is great
agegreaterthan = [x for x in cursor]
print(agegreaterthan)

'''
# https://stackoverflow.com/questions/11973725/how-to-efficiently-perform-distinct-with-multiple-keys
cursor = db.sap21.aggregate([{"$group":{"_id":{'mariners.name':"$mariners.name", 'mariners.age':"$mariners.age"}}}]);
mix = [x for x in cursor]
print(mix)

# https://stackoverflow.com/questions/44256377/multiple-field-distinct-aggregation-in-mongodb
cursor = db.sap21.aggregate([
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