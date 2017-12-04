# -*- coding: utf-8 -*-
"""
@author: sap21
"""


# exercise 1
def percentage_bikes(traffic_string):
    """Takes in a string of Traffic as a parameter and returns percentage of bikes.
    >>> percentage_bikes("BBCBLLMCCCSVSS")
        28.57142...
    """
    bikes_per = 0
    bikes = ["B", "M"]
    for t in ['B', 'C', 'L', 'M', 'S', 'T', 'V']:
        #print("percent of ", t, " is ", (traffic_string.count(t) / len(traffic_string)) * 100) # for all 
        if t in bikes:
          #print("% ", t, " = ", (traffic_string.count(t) / len(traffic_string)) * 100)  # for bikes
          bikes_per = bikes_per + ((traffic_string.count(t) / len(traffic_string)) * 100)  
    return bikes_per


#exercise 5

def main():
    """Main function demonstrating usage, functions in this script:
        percentage_bikes
        bridge_prices
        counts
        read_student_data
        write_traffic_data
        print_histogram
    """
    #question 1
    bikes = percentage_bikes("BBCBLLMCCCSVSSMMBCC")
    print(bikes)


if __name__ == "__main__":
    main()