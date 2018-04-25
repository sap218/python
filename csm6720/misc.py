# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 15:31:25 2018
@author: sap21

>> Please note: this work isn't for my CS assignment - content is somewhat related though.
"""

from pprint import pprint
from pymongo import MongoClient
import matplotlib.pyplot as plt

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

def plot_ship_records_count():
    plt.figure(1)
    fig = plt.figure(1)
    plt.style.use('fivethirtyeight')
    
    cursor = db.sap21.aggregate([{'$group':
        {'_id':'$vessel name', 'count':{'$sum':1}}}])
    values = [x['count'] for x in cursor]
    #print(values)
    plt.hist(values)
    plt.xlabel('Number of records for each ship', fontsize=12)
    plt.ylabel('Count of ships with N records', fontsize=12)
    plt.title('Distribution of number of records to each ship', fontsize=14)
    fig.savefig("test.png")
    plt.tight_layout()
    plt.show
                 
                 
if __name__ == "__main__":
    user = 'sap21'
    dbpath = 'nosql.dcs.aber.ac.uk/sap21'
    password = input('Enter Password...')
    connection_string = 'mongodb://'+user+':'+password+'@'+dbpath
    client = MongoClient(connection_string)
    db = client.sap21
    
    #list_ships() # does not work properly?
    #get_ship("Margaret Ann")  
    
    plot_ship_records_count()

    ##############################################
    # Other additional stuff I did for practice

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
    
    # Printing out mariner's names for those older than 60    
    cursor = db.sap21.distinct("mariners.name", {'mariners.age': {'$gte':60}}) 
    agegreaterthan = [x for x in cursor]
    print(agegreaterthan)