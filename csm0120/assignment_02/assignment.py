# -*- coding: utf-8 -*-
"""
@author: sap21
"""

import csv
import UKMap
import sqlite3
import sys
import requests
import bs4

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
def input_city_into_db(filename, db_conn):
    conn = sqlite3.connect(db_conn)
    c = conn.cursor()
    in_file = open(filename)
    csvreader = csv.reader(in_file)
    for row in csvreader:
        parameters = {"city":row[0],
                "latitude":row[1],
                "longitude":row[2]}
        query = """INSERT INTO latlon (city, latitude, longitude) 
        VALUES (:city,:latitude,:longitude)"""
        result = c.execute(query, parameters)
        conn.commit()
    '''try:
        conn = sqlite3.connect("noSuchDB.sqlite")
    except sqlite3.Error:
        print("The database does not exist")
        sys.exit(1)
        '''
    #result = c.execute(query, parameters)
    #conn.commit()
    conn.close()
    
def input_user_into_db(filename, db_conn):
    conn = sqlite3.connect(db_conn)
    c = conn.cursor()
    in_file = open(filename)
    csvreader = csv.reader(in_file)
    header_row = next(csvreader)
    for row in csvreader:
        parameters = {"nametitle":row[0],
                "namefirst":row[1],
                "namelast":row[2],
                "city":row[3],
                "email":row[4],
                "dob":row[5],
                "phone":row[6]
                }
        query = """INSERT INTO users (nametitle, namefirst, namelast, city, email, dob, phone) 
        VALUES (:nametitle,:namefirst,:namelast,:city,:email,:dob,:phone)"""
        result = c.execute(query, parameters)
        conn.commit()
    conn.close()    
    
################################################    

# exercise 3
def search_weather(term):
    url = "http://export.arxiv.org/api/query" # http://api.met.no/weatherapi/locationforecast/1.9/documentation
    payload = {"search_query":"all:"+term,
               "start":0,
               "max_results":10
               }
    response = requests.get(url, params=payload)
    
    if response.status_code == 200:
        return response.text
    else:
        return None
    
def print_tag_text(xml_text, tag_name):
    soup = bs4.BeautifulSoup(xml_text, "xml")
    tags = soup.select("feed > entry > "+tag_name)
    for tag in tags:
print(tag.text)

################################################
    
def main():
    #plot_all_towns("latlon.csv")
    #input_city_into_db("latlon.csv", "csm0120_database.sqlite")
    #input_user_into_db("users.csv", "csm0120_database.sqlite")
    '''
    xml_response = search_weather("aberystwyth")
    if xml_response is None:
        print("bad response from weather api")
    else:
        print_tag_text(xml_response, "title")
    '''

if __name__ == "__main__":
    main()