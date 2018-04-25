# -*- coding: utf-8 -*-
"""
CSM6720
@author: sap21

>> Plotting crew ranks & location popularity
"""

from pymongo import MongoClient
import matplotlib.pyplot as plt
from collections import Counter

def plot_ranks(): # setting up function
    cursor = db.sap21.aggregate([
        {"$match": {"mariners.this_ship_capacity": {"$nin": ["Blk", "blk", "blk ", "Blk "]}}},
        {"$unwind":"$mariners"},
        {"$group": {
            "_id": {
                "rank": "$mariners.this_ship_capacity"
            },
            "count": {"$sum": 1}
        }}
    ]) # removing all blanks whilst gathering all ranks together
    ranks = []
    deltab = "[]()1234567890,$-:" # removing these numbers and special characters
    trantab = str.maketrans("", "", deltab) 
    for mariner_jobs in cursor:
        mariner_jobs = str(mariner_jobs['_id'].get('rank', '')).lower()
        amper_jobs = mariner_jobs.split("&")
        and_jobs = mariner_jobs.split("and")    
        slash_jobs = mariner_jobs.split("/")
        plus_jobs = mariner_jobs.split("+")

        if len(amper_jobs) > 1: 
            jobs = amper_jobs
        elif len(and_jobs) > 1:
            jobs = and_jobs
        elif len(slash_jobs) > 1:
            jobs = slash_jobs
        elif len(plus_jobs) > 1:
            jobs = plus_jobs
        else:
            jobs = [mariner_jobs]            
        for job in jobs:
            ranks.append(job.strip().replace("2nd", "second").replace("1st", "first").replace("3rd", "third").lower(
        ).translate(trantab).strip()) # ensuring 1st, 2nd, and 3rd remain
    counting_ranks = Counter(ranks)
    plots = counting_ranks.most_common(30) # gaining top 30
    del plots[8] # blank        
    final_ranks = dict(plots)  
    final_ranks['lamptrimmer'] += final_ranks['lamps'] # combining same ranks in order to remove one
    final_ranks['lamptrimmer'] += final_ranks['trimmer']
    del final_ranks['lamps'] # this is the removing part
    del final_ranks['trimmer']
    final_ranks['able seaman'] += final_ranks['able seamen']
    del final_ranks['able seamen']  
    final_ranks['engineer'] += final_ranks['th engineer']
    del final_ranks['th engineer']
    #del final_ranks['lps']
    
    # setting up the order of the list
    order = ['boy','purser','sailor','seaman','ordinary seaman','able seaman',
             'lamptrimmer','carpenter','boatswain','bosun','mess room steward',
             'cook','steward','cook steward','fireman','donkeyman','engineer', 'third engineer',
             'second engineer','first engineer','mate','second mate','first mate','master']
    # sometimes purser should be changed to apprentice

    numbers = []
    for job in order:
        numbers.append(final_ranks[job]) # putting the numbers into a list based on the order I chose to rank   
    #print(final_ranks)
    plt.figure(1)
    fig = plt.figure(1)
    plt.style.use('fivethirtyeight')
    plt.bar(range(len(order)), numbers, tick_label=order)
    plt.xlabel('Rank Title', fontsize=12)  
    plt.xticks(rotation=75, fontsize=8)
    plt.ylabel('Count', fontsize=12)
    plt.yticks(fontsize=10)
    plt.title('Distribution of Crew Rankings', fontsize=14)
    fig.savefig('ranks.png')
    plt.tight_layout()
    plt.show()  

def plot_locations():
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
    ]) # gaining all locations from last, join, and leaving port
    deltab = "[]()1234567890,$-:"
    trantab = str.maketrans("", "", deltab)
    for r in results:
        ports.append(r['_id'].get('lastport'))
        ports.append(r['_id'].get('joiningport'))
        ports.append(r['_id'].get('leaveport'))    
    for i, p in enumerate(ports):
        try:
            ports[i] = ports[i].translate(trantab)
        except AttributeError: # using error handling 
            continue
    counting_ports = Counter(ports)
    port_count = counting_ports.most_common(20) # gaining top 20 results 
    port_count = dict(port_count) 
    port_count['Aberystwyth'] += port_count['Aberystwith']    
    del port_count['Aberystwith']  
    del port_count['Aberystwyth'] # remove this if want to compare to Aberystwyth 
    del port_count['Continued'] 
    port_count['Porthmadog'] += port_count['Portmadoc']
    del port_count['Portmadoc']
    plt.figure(2)
    fig = plt.figure(2)
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


if __name__ == "__main__":
    """
    Main function demonstrating usage of functions in this script.
    """
    user = 'sap21'
    dbpath = 'nosql.dcs.aber.ac.uk/sap21'
    password = input('Enter Password...')
    connection_string = 'mongodb://'+user+':'+password+'@'+dbpath
    client = MongoClient(connection_string)
    db = client.sap21
    
    plot_ranks() # task 1 - plotting ranks
    plot_locations() # task 2 - plotting popular locations