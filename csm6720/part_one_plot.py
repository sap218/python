# -*- coding: utf-8 -*-
"""
CSM6720
@author: sap21

>> Crew Ranks
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
    
    cursor = db.sap21.aggregate([
        {"$match": {"mariners.this_ship_capacity": {"$nin": ["Blk", "blk", "blk ", "Blk "]}}},
        {"$unwind":"$mariners"},
        {"$group": {
            "_id": {
                "rank": "$mariners.this_ship_capacity"
            },
            "count": {"$sum": 1}
        }}
    ])

    ranks = []
    deltab = "[]()1234567890,$-:"
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
        ).translate(trantab).strip())
    
    counting_ranks = Counter(ranks)
    plots = counting_ranks.most_common(30)
    
    del plots[8] # blank        
    final_ranks = dict(plots)  
    
    final_ranks['lamptrimmer'] += final_ranks['lamps'] 
    final_ranks['lamptrimmer'] += final_ranks['trimmer']
    del final_ranks['lamps']   
    del final_ranks['trimmer']
    final_ranks['able seaman'] += final_ranks['able seamen']
    del final_ranks['able seamen']  
    final_ranks['engineer'] += final_ranks['th engineer']
    del final_ranks['th engineer']
    del final_ranks['lps']
        
    order = ['boy','purser','sailor','seaman','ordinary seaman','able seaman',
             'lamptrimmer','carpenter','boatswain','bosun','mess room steward',
             'cook','steward','cook steward','fireman','donkeyman','engineer', 'third engineer',
             'second engineer','first engineer','mate','second mate','first mate','master'] # sometimes purser should be changed to apprentice
    numbers = []
    for job in order:
        numbers.append(final_ranks[job])        
     
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
    