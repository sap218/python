# -*- coding: utf-8 -*-
"""
This module focuses on locations, forecasts, and plotting.
@author: sap21
"""

import csv
import UKMap
import sqlite3
import sys
import requests
import bs4
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
    """Takes a latitude and longitude of a city - connects to MET Norway API and returns weather information.
    Saves the xml and returns a beautiful soup object.
    <<Data from MET Norway>>
    """
    url = "http://api.yr.no/weatherapi/locationforecast/1.9/?"
    payload = {"lat":+lat,
               "lon":+lon
               } # e.g. http://api.met.no/weatherapi/locationforecast/1.9/?lat=60.10;lon=9.58
    response = requests.get(url, params=payload)

    if response.status_code == 200: 
        soup = bs4.BeautifulSoup(response.text, "xml")
        f = open("coordinate_forecast.xml", "w")
        f.write(soup.prettify())
        f.close()
        return soup
    else:
        return None

################################################    

# exercise 4
def wind_forecast(soup, tag, att):
    """Takes in a soup object and a tag name plus an attribute.
    Returns time stamps, plus the datalist.
    """
    timelist = []
    datalist = []
    forecasts = soup.find_all("time")
    format = "%Y-%m-%dT%H:%M:%SZ"    
    for f in forecasts:
        t = datetime.datetime.strptime(f["from"], format)       
        ftags = f.find_all(tag) 
        for ftag in ftags:
            timelist.append(t)
            datalist.append(float(ftag[att]))  
    return (timelist, datalist)
    
def plot_winds(times, windspeedlist, coordinates):
    """Takes in a list of times and a datalist of windspeed to plot a graph. 
    """
    plt.plot(times, windspeedlist, 'c-')
    plt.title('Line graph of windspeed against time at (%f, %f)' % (coordinates[0], coordinates[1]), fontsize=10)
    plt.xlabel('Time', fontsize=7.5)
    plt.ylabel('Wind Speed (mps)', fontsize=7.5)
    plt.xticks(fontsize=6.5, rotation=17.5)
    plt.yticks(fontsize=6.5)
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
   
def plot_user_windspeeddirection(coord1, coord2, user_wind):
    """Takes in coordinates and the dataset of wind information from the user's city.
    Plots a graph of their location and icon depends on wind speed, plus direction.
    """
    colors = ['blue', 'green', 'yellow', 'orange', 'red']       
    top = max(user_wind[0]) + 1
    step = top / len(colors)
    speed = user_wind[0][0]
    x = int(speed/step)
   
    mp = UKMap.UKMap()
    mp.plot(coord2, coord1, marker=(3, 0, int(user_wind[1][0])), color=colors[x], markersize=10)
    mp.plot(coord2, coord1, marker=(2, 0, int(user_wind[1][0])), color='dimgrey', markersize=20) # flair: line to show proper direction of wind
    mp.savefig("user_weather.png") # flair: saving figure    
    mp.show()

################

def user_forecast_map(email, db):
    """Function that calls in the other functions: takes in an database parameter to connect to the database.
    Uses an email to find the city of a user, then uses that city to find coordinates.
    Checks weather forecast of WindSpeed and Direction of that city, saves the xml.
    Then plots the information.
    """
    city = user_loc(email, db)
    coord = loc_coord(city, db)

    if coord is not None:
        soup_user = forecast(coord[0], coord[1])
        if soup_user is None:
            print("Bad response from weather api")
        else:
            winddir = wind_forecast(soup_user, "windSpeed", "mps")
            windspd = wind_forecast(soup_user, "windDirection", "deg")
                    
        f = open("user_city_windspeed_direction.xml", "w")
        f.write(soup_user.prettify())
        f.close()
            
        plot_user_windspeeddirection(coord[0], coord[1], (windspd[1], winddir[1]))
    else:
        print("User city coordinates not in database to plot")

################################################    
################################################ 

def main():
    """Main function demonstrating usage of functions in this script.
    """
    #plt.figure(1)
    #plot_all_towns("latlon.csv") # ex 1
    
    #input_city_into_db("latlon.csv", "csm0120_database.sqlite") # ex 2
    #input_user_into_db("users.csv", "csm0120_database.sqlite") # these two lines take a while to run
    
    coords = (52.41616, -4.064598)
    soup = forecast(coords[0], coords[1]) # ex 3    
    forecasts = soup.find_all("time", datatype="forecast")
    for f in forecasts:
        print(f.prettify())
             
    (times, windspeeds) = wind_forecast(soup, "windSpeed", "mps") # ex 4
    plt.figure(2)
    with plt.style.context('ggplot'): # flair: changing style of plot | print(plt.style.available)
        plot_winds(times, windspeeds, coords)   
    '''
    plt.figure(3)
    user_forecast_map("marie.howard@example.com", "csm0120_database.sqlite") # ex 5
    '''
################################################ 

if __name__ == "__main__":
    main()