# -*- coding: utf-8 -*-
"""
CSM6720
@author: sap21

>> Most popular location destinations/ports for vessels 
"""

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

    ports = []
    results = db.sap21.aggregate([
        {"$match": {"mariners.last_ship_port": {"$nin": ["Blk", "blk", "blk ", "Blk "]}}},
        {"$match": {"mariners.this_ship_joining_port": {"$nin": ["Blk", "blk", "blk ", "Blk "]}}},
        {"$match": {"mariners.this_ship_leaving_port": {"$nin": ["Blk", "blk", "blk ", "Blk "]}}},
        {"$unwind":"$mariners"},
        {"$group": {
            "_id": {
                "lastport": "$mariners.last_ship_port",
                "joiningport": "$mariners.this_ship_joining_port",
                "leaveport": "$mariners.this_ship_leaving_port"
            },
            "count": {"$sum": 1}
        }}
    ])
    
    deltab = "[]()1234567890,$-:"
    trantab = str.maketrans("", "", deltab)
    
    for r in results:
        ports.append(r['_id'].get('lastport'))
        ports.append(r['_id'].get('joiningport'))
        ports.append(r['_id'].get('leaveport'))
        
    for i, p in enumerate(ports):
        try:
            ports[i] = ports[i].translate(trantab)
        except AttributeError:
            continue
    
    counting_ports = Counter(ports)
    port_count = counting_ports.most_common(20)
    port_count = dict(port_count) 
    
    port_count['Aberystwyth'] += port_count['Aberystwith']    
    del port_count['Aberystwith']   
    del port_count['Continued'] 
    port_count['Porthmadog'] += port_count['Portmadoc']
    del port_count['Portmadoc']
   
    plt.figure(1)
    fig = plt.figure(1)
    plt.style.use('fivethirtyeight')
    plt.bar(port_count.keys(), port_count.values())
    plt.xlabel('Location', fontsize=12)  
    plt.xticks(fontsize=8)
    plt.xticks(rotation=75)
    plt.ylabel('Count', fontsize=12)
    plt.yticks(fontsize=10)
    plt.title('Distribution of Location Popularity', fontsize=14)
    fig.savefig('location.png')
    plt.tight_layout()
    plt.show()  