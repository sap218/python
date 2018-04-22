# -*- coding: utf-8 -*-
"""
CSM6720
@author: sap21
"""

from pprint import pprint
from pymongo import MongoClient
import matplotlib.pyplot as plt
'''
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
'''               
                     
if __name__ == "__main__":
    user = 'sap21'
    dbpath = 'nosql.dcs.aber.ac.uk/sap21'
    password = input('Enter Password...')
    connection_string = 'mongodb://'+user+':'+password+'@'+dbpath
    client = MongoClient(connection_string)
    db = client.sap21
    
    #list_ships()
    #get_ship("Margaret Ann")  
