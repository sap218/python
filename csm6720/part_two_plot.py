# -*- coding: utf-8 -*-
"""
CSM6720
@author: sap21
"""

from pprint import pprint
from pymongo import MongoClient
import matplotlib.pyplot as plt
from collections import Counter

if __name__ == "__main__":
    user = 'sap21'
    dbpath = 'nosql.dcs.aber.ac.uk/sap21'
    password = input('Enter Password...')
    connection_string = 'mongodb://'+user+':'+password+'@'+dbpath
    client = MongoClient(connection_string)
    db = client.sap21
    
    ##################################################    
    
    "this_ship_joining_port"
    "this_ship_leaving_port"    
    "place_of_birth"    
    "last_ship_port"
    
    '''   
    #cursor = db.sap21.find({"mariners.last_ship_port": {"$all":[]}})
    cursor = db.sap21.find({"mariners.last_ship_port": []})
    places = []
    for r in cursor:
        places.append(r)
    pprint(places)
    '''
    #####    
    
    cursor = db.sap21.distinct("mariners.last_ship_port")
    ports = [] 
        
    deltab = "[]()1234567890,$-:"
    #intab = ""
    #outtab = ""
    trantab = str.maketrans("", "", deltab)
         
    for p in cursor:
        ports.append(str(p).lower.strip().translate(trantab))    
   
    print(ports)   
    '''
    counting_ports = Counter(ports)
    plots = counting_ports.most_common(10)

    del plots[8] # blank 8
    del plots[15] # lamps 16 
    del plots[19] # trimmer 21
    del plots[20] # able seamen 23
    del plots[20] # th engineer 24
    
    final_ports = dict(plots)  
    '''