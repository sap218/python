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
    Connects to MET Norway API and returns weather information.
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
    """Takes in an xml and a tag name,
    Looks through the xml and searching for the tag term then displays output.
    """
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
    """Takes in a list of wind speed and plots the graph. 
    """
    #plt.style.use('ggplot') # flaur: changing style of plot | print(plt.style.available)
    plt.plot(range(len(list)), list, 'c-')
    plt.xlabel('Time')
    plt.ylabel('Wind Speed (mps)')
    plt.xticks([])
    #plt.yticks(rotation=11, tick_spacing=1)
    plt.savefig("windplot.png") # flair: saving figure
    plt.show()

################################################

def user_loc(email, db_conn):
    """Takes in an email along with the database connection.
    Returns the users' city from the email address.
    """
    conn = sqlite3.connect(db_conn)
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    q_email = email    
    query = """SELECT * FROM users
        WHERE email = ?"""
    parameters = (q_email, )
    try:
        result = c.execute(query, parameters)
    except sqlite3.Error as e:
        print(e.args[0])
        sys.exit(1)  
    else:
        for row in result:
            #print ("Details: " + row["email"] + " = " + row["city"])
            return str(row["city"])
    conn.close()

#################

def loc_coord(city, db_conn):
    """Takes in a city and looks for the co-ordinates from the city table of the database.
    Returns co-ordinates for that city.
    """
    conn = sqlite3.connect(db_conn)
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    q_city = city.capitalize()    
    query = """SELECT * FROM latlon
        WHERE city = ?"""
    parameters = (q_city, )
    try:
        result = c.execute(query, parameters)
    except sqlite3.Error as e:
        print(e.args[0])
        sys.exit(1)  
    else:
        for row in result:
            #print (row["latitude"] + row["longitude"])
            return (row["latitude"], row["longitude"])   
    conn.close() 
    

################

def user_forecast(xml_text, wndspd, wnddir): 
    user_windspeedlist = []
    user_winddirectionlist = []    
    
    soup = bs4.BeautifulSoup(xml_text, "xml")
    
    windspeed = soup.find_all(wndspd)
    for windspeed in windspeed:
        string = str(windspeed)
        string = string.replace('<windSpeed beaufort="4" id="ff" mps="',"")
        string = string.replace('<windSpeed beaufort="5" id="ff" mps="',"")
        string = string.replace('<windSpeed beaufort="3" id="ff" mps="',"")
        string = string.replace('<windSpeed beaufort="6" id="ff" mps="',"")
        string = string.replace('<windSpeed beaufort="2" id="ff" mps="',"")
        string = string.replace('" name="Laber bris"/>',"")
        string = string.replace('" name="Frisk bris"/>',"")
        string = string.replace('" name="Svak vind"/>',"")
        string = string.replace('" name="Lett bris"/>',"")
        string = string.replace('" name="Liten kuling"/>',"")
        user_windspeedlist.append(string)
    #print(len(user_windspeedlist), user_windspeedlist)
    
    winddir = soup.find_all(wnddir)
    for winddir in winddir:
        string = str(winddir)
        string = string.replace('<windDirection deg="',"")
        string = string.replace('" id="dd" name="W"/>',"")
        string = string.replace('" id="dd" name="SW"/>',"")
        string = string.replace('" id="dd" name="S"/>',"")
        string = string.replace('" id="dd" name="NW"/>',"")
        string = string.replace('" id="dd" name="SE"/>',"")
        string = string.replace('" id="dd" name="NE"/>',"")
        string = string.replace('" id="dd" name="N"/>',"")
        user_winddirectionlist.append(string)
    #print(len(user_winddirectionlist), user_winddirectionlist)    
    
    return (user_windspeedlist, user_winddirectionlist)
   

################################################    

def main():
    """Main function demonstrating usage, functions in this script:
        plot_all_towns() 
        input_city_into_db() 
        input_user_into_db()
        search_weather() with print_text() & wind_forecast() with plot_winds()
        user_loc() with loc_coord()
        tree.write() is also an additional function to export the xml
        
    """
    #plot_all_towns("latlon.csv") # ex 1
    #input_city_into_db("latlon.csv", "csm0120_database.sqlite") # ex 2
    #input_user_into_db("users.csv", "csm0120_database.sqlite") # ex 2
    '''
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
    '''

    city = user_loc("rebecca.baker@example.com", "csm0120_database.sqlite") # ex 5
    coord = loc_coord(city, "csm0120_database.sqlite")
    xml_user = search_weather(51.45, -2.59)
    if xml_user is None:
        print("bad response from weather api")
    else:
        user_wind = user_forecast(xml_user, "windSpeed", "windDirection")

    #plt.plot(user_wind[0], user_wind[1], 'ro')
    #plt.show()

    mp = UKMap.UKMap()        
    #mp.plot(-2.59, 51.45, 'bs')
    mp.plot(-2.59, 51.45, marker='o')
    #mp.plot(51.45, -2.59, 'bs', user_wind[0], user_wind[1], 'ro')
    mp.show

if __name__ == "__main__":
    main()