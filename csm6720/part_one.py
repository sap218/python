# -*- coding: utf-8 -*-
"""
CSM6720
@author: sap21
"""

from pprint import pprint
from pymongo import MongoClient

def list_ships(): # set up a function to list ship names
    records = db.sap21.aggregate([ 
        {"$group": {
            "_id": {
                "vessel name": "$vessel name"
            },
            #"count": {"$sum": 1} # counting how many times appear
        }}, 
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]) 
    for r in records:
        print(r)
      
def get_ship(ship_name): # function to get information on a ship
    records = db.sap21.find({"vessel name": ship_name})
    for r in records:
        print(r["vessel name"], r["official number"])        

def get_ship_mates():
    records = db.sap21.aggregate([
        {"$match": {"mariners.year_of_birth": {"$nin": ["Blk", "blk"]}}},
        {"$unwind":"$mariners"},
        {"$group": {
            "_id": {
                "name": "$mariners.name",
                "year_of_birth":"$mariners.year_of_birth",
                "place_of_birth": "$mariners.place_of_birth"
            },
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 20}
    ])
    for r in records:
        print(r)
    
def get_mariner(mariner_name, year_of_birth):
    records = db.sap21.find({"mariners.name": mariner_name, "mariners.year_of_birth": year_of_birth})
    count = 0    
    for r in records:
        count += 1
        #pprint(r)
        print(r["vessel name"])
        try:
            for m in r["mariners"]:
                if m['name'] == mariner_name:
                    pprint(m)
        except KeyError:
            continue
    print("%d records returned" % count)
                     
if __name__ == "__main__":
    user = 'sap21'
    dbpath = 'nosql.dcs.aber.ac.uk/sap21'
    password = input('Enter Password...')
    connection_string = 'mongodb://'+user+':'+password+'@'+dbpath
    client = MongoClient(connection_string)
    db = client.sap21
    
    list_ships()
    #get_ship("Margaret Ann")
    #get_ship_mates()
    #get_mariner("John Davies", 1840)    