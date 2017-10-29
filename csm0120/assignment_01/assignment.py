# -*- coding: utf-8 -*-
"""
@author: sap21
"""

# exercise 1

def percentage_bikes(traffic_string):
    bikes_per = 0
    bikes = ["B", "M"]
    for t in ['B', 'C', 'L', 'M', 'S', 'T', 'V']:
        #print("percent of ", t, " is ", (traffic_string.count(t) / len(traffic_string)) * 100) # for all 
        if t in bikes:
          #print("% ", t, " = ", (traffic_string.count(t) / len(traffic_string)) * 100)  # for bikes
          bikes_per = bikes_per + ((traffic_string.count(t) / len(traffic_string)) * 100)  
    return bikes_per


# exercise 3 
def counts(traffic_string):
    traffic_count = []
    for t in ['B', 'C', 'L', 'M', 'S', 'T', 'V']: # order changed
        traffic_count.append(traffic_string.count(t))
    return traffic_count