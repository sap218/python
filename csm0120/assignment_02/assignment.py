# -*- coding: utf-8 -*-
"""
@author: sap21
"""

import csv
import UKMap
import sqlite3

# exercise 1
def plot_all_towns(filename):
    mp = UKMap.UKMap()        
    coordinates = open(filename)
    csvreader = csv.reader(coordinates)
    for line in csvreader:
        mp.plot(float(line[2]),float(line[1]))
        mp.show
        #print(line) # flair: prints out every line
    mp.savefig("map.png") # flair: saving figure
    coordinates.close()
    
################################################    

# exercise 2
# Connect to database
conn = sqlite3.connect("csm0120_database.sqlite")

#for i in csvreader, range(row):
#    pass
#    i = i+1

parameters = {"city":list[0],
              "longitude":list[1]",
              "latitude":list[2]}
    query = """INSERT INTO user (cite, longitude, latitude) 
    VALUES (:city,:longitude,:latitude)"""
    result = c.execute(query, parameters)
#try: 
    #result = c.execute(query, parameters)
    #conn.commit()
conn.commit()

conn.close()

################################################
    
def main():
    plot_all_towns("latlon.csv")

if __name__ == "__main__":
    main()