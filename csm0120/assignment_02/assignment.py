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
'''
# exercise 2
def input_into_db(filename, db_conn):
    conn = sqlite3.connect("csm0120_database.sqlite")
    in_file = open(filename)
    csvreader = csv.reader(in_file)
    for row in csvreader:
        parameters = {"city":row[0],
                  "longitude":row[1]",
                  "latitude":row[2]}
        query = """INSERT INTO user (cite, longitude, latitude) 
        VALUES (:city,:longitude,:latitude)"""
        result = c.execute(query, parameters)

    #    try:
    #       execute the query with params
    #    except SQLite.Error:
    #       deal with the error

    #try: 
        #result = c.execute(query, parameters)
        #conn.commit()
    conn.commit()

    conn.close()
'''
################################################
    
def main():
    plot_all_towns("latlon.csv")
    #input_into_db("latlon.csv", "csm0120_database.sqlite")


if __name__ == "__main__":
    main()