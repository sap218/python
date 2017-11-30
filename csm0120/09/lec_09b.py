#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:19:10 2017

@author: sap21
"""

import bs4
import requests
url = "http://api.yr.no/weatherapi/locationforecast/1.9/"
payload = {"lat" : 52.41616,
           "lon" : -4.064598 
           }
response = requests.get(url, params=payload)
if response.status_code == 200: 
    xml_text = response.text
    soup = bs4.BeautifulSoup(xml_text, "xml")
    forecasts = soup.find_all("time", datatype="forecast")
    for forecast in forecasts:
        print(forecast.prettify())

'''
temperatures = soup.find_all("temperature")
for t in temperatures:
    print(t.get("value") + " "+ t.get("unit"))
'''


url = "https://en.wikipedia.org/w/api.php"
payload = {"format":"json",
           "action":"query",
           "prop":"extracts",
           "exintro":"",
           "explaintext":"",
           "titles":"london"
           }
response = requests.get(url, params=payload)
if response.status_code == 200:
    results = response.json()
    pages = results['query']['pages']
    for page in pages:
        print(results['query']['pages'][page]['extract'])