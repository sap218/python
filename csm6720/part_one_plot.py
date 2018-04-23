# -*- coding: utf-8 -*-
"""
CSM6720
@author: sap21
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
    
    deltab = "[]()1234567890,$-:"
    #intab = ""
    #outtab = ""
    trantab = str.maketrans("", "", deltab)
    
    cursor = db.sap21.distinct("mariners.this_ship_capacity")

    ranks = []
    for mariner_jobs in cursor:
        mariner_jobs = str(mariner_jobs).lower()
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
    counting_ranks.most_common()
    #for k, v in counting_ranks.most_common(10):
        #print ('%s: %i' % (k, v))    

    plots = counting_ranks.most_common(27)
    
    del plots[8] # blank 8
    del plots[15] # lamps 16 
    del plots[19] # trimmer 21
    del plots[20] # able seamen 23
    del plots[20] # th engineer 24

    final_ranks = dict(plots)  
    
    order = ['boy','apprentice','sailor','seaman','ordinary seaman','able seaman',
             'lamptrimmer','carpenter','boatswain','bosun','mess room steward',
             'cook','steward','cook steward','fireman','donkeyman','engineer',
             'second engineer','first engineer','second mate','mate','master']
             
    numbers = []
    for job in order:
        numbers.append(final_ranks[job])        

    plt.figure(1)
    fig = plt.figure(1)
    plt.style.use('fivethirtyeight')
    plt.bar(range(len(order)), numbers, tick_label=order)
    plt.xlabel('Rank')  
    plt.xticks(fontsize=8)
    plt.xticks(rotation=75)
    plt.ylabel('Count')
    plt.title('Distribution of Crew Rankings')
    fig.savefig('ranks.png')
    plt.tight_layout()
    plt.show()  