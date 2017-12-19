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
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# exercise 1
def plot_all_towns(filename):
    """Takes in a file (csv) of latitude and longitudes of UK cities.
    Then uses another python module: UKMap to plot cities on the map.
    """
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
    """Takes in a file name with city, latitude, and longitude.
    Connects to the cities database and inputs them.
    """
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
    """Takes in a filename of users.
    Connects to the users database and inputs them.
    """
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
def search_weather(lat, lon):  # http://api.met.no/weatherapi/locationforecast/1.9/documentation
    """Takes a latitude and longitude of a city.
    Connects to MET Norway API and returns weather information
    «Data from MET Norway»
    """
    url = "http://api.yr.no/weatherapi/locationforecast/1.9/?"
    payload = {"lat":+lat,
               "lon":+lon
               } # http://api.met.no/weatherapi/locationforecast/1.9/?lat=60.10;lon=9.58
    response = requests.get(url, params=payload)

    if response.status_code == 200: 
        return response.text
    else:
        return None
        
def print_text(xml_text): 
    """Takes in an xml and uses the package: Beautiful Soup.
    This returns the xml in a pretty format.
    """
    soup = bs4.BeautifulSoup(xml_text, "xml")
    forecasts = soup.find_all("time", datatype="forecast")
    for forecast in forecasts:
        print(forecast.prettify())

################################################    

# exercise 4

def wind_forecast(xml_text, tag_name): 
    windlist = []
    soup = bs4.BeautifulSoup(xml_text, "xml")
    forecasts = soup.find_all(tag_name)
    for forecast in forecasts:
        string = str(forecast)
        string = string.replace('<windSpeed beaufort="3" id="ff" mps="',"")
        string = string.replace('<windSpeed beaufort="5" id="ff" mps="',"")
        string = string.replace('<windSpeed beaufort="1" id="ff" mps="',"")
        string = string.replace('<windSpeed beaufort="2" id="ff" mps="',"")
        string = string.replace('<windSpeed beaufort="4" id="ff" mps="',"")
        string = string.replace('" name="Laber bris"/>',"")
        string = string.replace('" name="Lett bris"/>',"")
        string = string.replace('" name="Svak vind"/>',"")
        string = string.replace('" name="Flau vind"/>',"")
        string = string.replace('" name="Frisk bris"/>',"")
        #print(string)
        windlist.append(string)
    #print(len(windlist), windlist)
    return windlist

def plot_winds(list):
    plt.style.use('ggplot') # flaur: changing style of plot | print(plt.style.available)
    plt.plot(range(len(list)), list, 'c-')
    plt.xlabel('Time')
    plt.ylabel('Wind Speed (mps)')
    plt.xticks([])
    #plt.yticks(rotation=11, tick_spacing=1)
    plt.savefig("windplot.png") # flair: saving figure
    plt.show()

################################################
    
def main():
    """Main function demonstrating usage, functions in this script:
        plot_all_towns() 
        input_city_into_db() 
        input_user_into_db()
        search_weather() with print_text() and wind_forecast()
    """
    #plot_all_towns("latlon.csv") # ex 1
    #input_city_into_db("latlon.csv", "csm0120_database.sqlite") # ex 2
    #input_user_into_db("users.csv", "csm0120_database.sqlite") # ex 2

    xml_response = search_weather(52.41616, -4.064598) # ex 3
    if xml_response is None:
        print("bad response from weather api")
    else:
        print_text(xml_response)
        windlist = wind_forecast(xml_response, "windSpeed") # ex 4
    
    tree = ET.ElementTree(ET.fromstring(xml_response)) # flair: making an xml file
    root = tree.getroot()
    tree.write('output.xml') 

    plot_winds(windlist) # ex 4


if __name__ == "__main__":
    main()