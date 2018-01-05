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
import datetime

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
def forecast(lat, lon):  # http://api.met.no/weatherapi/locationforecast/1.9/documentation
    """Takes a latitude and longitude of a city.
    Connects to MET Norway API and returns weather information.
    «Data from MET Norway»
    Saves the xml and returns a beautiful soup object
    """
    url = "http://api.yr.no/weatherapi/locationforecast/1.9/?"
    payload = {"lat":+lat,
               "lon":+lon
               } # http://api.met.no/weatherapi/locationforecast/1.9/?lat=60.10;lon=9.58
    response = requests.get(url, params=payload)

    if response.status_code == 200: 
        #return response.text
        soup = bs4.BeautifulSoup(response.text, "xml")
        f = open("coordinate_forecast.xml", "w")
        f.write(soup.prettify())
        f.close()
        return soup
    else:
        return None

################################################    

# exercise 4

def wind_forecast(soup):
    timelist = []
    windspeedlist = []
    forecasts = soup.find_all("time")
    #print(forecasts)
    format = "%Y-%m-%dT%H:%M:%SZ"
    
    for f in forecasts:
        t = datetime.datetime.strptime(f["from"], format) 
        #print(f)        
        if f.windSpeed:
            timelist.append(t)
            windspeedlist.append(float(f.windSpeed["mps"]))  
      
        
    #print (timelist)
    return (timelist, windspeedlist)
    
def plot_winds(times, windlist, coordinates):
    """Takes in a list of times and wind speeds and plots the graph. 
    """
    plt.style.use('seaborn-poster') # flair: changing style of plot | print(plt.style.available)
    plt.plot(times, windlist, 'c-')
    plt.title('Line graph of windspeed against time at (%f, %f)' % (coordinates[0], coordinates[1]))
    plt.xlabel('Time', fontsize=14)
    plt.ylabel('Wind Speed (mps)', fontsize=14)
    plt.xticks(fontsize=11, rotation=15)
    plt.yticks(fontsize=11)
    plt.savefig("windplot.png") # flair: saving figure
    plt.show()

################################################

# exercise 5

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
            return (row["latitude"], row["longitude"])   
    conn.close() 

def user_forecast(xml_text, wndspd, wnddir): 
    """Searches for windspeed and wind direction from xml text and returns lists. 
    """################
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
        string = string.replace('" id="dd" name="E"/>',"")
        user_winddirectionlist.append(string)
    #print(len(user_winddirectionlist), user_winddirectionlist)    
    user_windspeedlist = [float(i) for i in user_windspeedlist]
    user_winddirectionlist = [float(i) for i in user_winddirectionlist]    
    
    return (user_windspeedlist, user_winddirectionlist)
   
################
   
def plot_user_windspeeddirection(coord1, coord2, user_wind):

    colors = ['blue', 'green', 'yellow', 'orange', 'red']       
    top = max(user_wind[0]) + 1
    step = top / len(colors)
    speed = user_wind[0][0]
    x = int(speed/step)
   
    mp = UKMap.UKMap()        
    mp.plot(coord2, coord1, marker=(3, 0, int(user_wind[1][0])), color=colors[x], markersize=10)
    mp.plot(coord2, coord1, marker=(2, 0, int(user_wind[1][0])), color='dimgrey', markersize=20) # flair: line to show direction
    mp.savefig("user_weather.png") # flair: saving figure    
    mp.show

################

def user_forecast_map(email, db):
    
    city = user_loc(email, db)
    coord = loc_coord(city, db)

    if coord is not None:
        xml_user = search_weather(coord[0], coord[1])
        if xml_user is None:
            print("bad response from weather api")
        else:
            user_wind = user_forecast(xml_user, "windSpeed", "windDirection")
            
        tree = ET.ElementTree(ET.fromstring(xml_user))
        root = tree.getroot()
        tree.write('user_city_windspeed_direction.xml') 
            
        plot_user_windspeeddirection(coord[0], coord[1], user_wind)
    else:
        print("User city coordinates not in database to plot")

################################################    
################################################ 

def main():
    """Main function demonstrating usage of functions in this script.
    """
    #plot_all_towns("latlon.csv") # ex 1
    #input_city_into_db("latlon.csv", "csm0120_database.sqlite") # ex 2
    #input_user_into_db("users.csv", "csm0120_database.sqlite") # ex 2
    
    #xml_response = forecast(52.41616, -4.064598) # ex 3
    
    
    coords = (52.41616, -4.064598)
    soup = forecast(coords[0], coords[1]) # ex 3    
    forecasts = soup.find_all("time", datatype="forecast")
    for f in forecasts:
        print(f.prettify())
             
    #windlist = wind_forecast(soup, "windSpeed") # ex 4
    (times, windspeeds) = wind_forecast(soup) # ex 4
    plot_winds(times, windspeeds, coords)
    
    #user_forecast_map("eleanor.allen@example.com", "csm0120_database.sqlite") # ex 5

################################################ 

if __name__ == "__main__":
    main()