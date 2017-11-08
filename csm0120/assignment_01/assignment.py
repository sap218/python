# -*- coding: utf-8 -*-
"""
@author: sap21
"""

import csv
from transpose import transpose


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

# exercise 2
def bridge_prices(traffic_string):
    """Takes in a string of Traffic as a paramter and returns the total price of bridge toll.
    >>> bridge_prices("BBCBLLMCCCSVSS")
        '£23.30'
    """
    total = 0
    price = {"B":0, "C":2, "L":5.5, "M":0.8, "S":0, "T":1, "V":3.5}
    for t in price:
        total = total + (traffic_string.count(t) * price[t])
    return "£%.2f" % total    
        
# exercise 3 
def counts(traffic_string):
    """Takes in a string of Traffic as a paramter and returns a total count of all types of vehicles.
    Returns in order: ['B', 'C', 'L', 'M', 'S', 'T', 'V']
    >>> counts("BBCBLLMCCCSVSS")
        [3, 4, 2, 1, 3, 0, 1]
    """
    traffic_count = []
    for t in ['B', 'C', 'L', 'M', 'S', 'T', 'V']:
        traffic_count.append(traffic_string.count(t))
    return traffic_count


# exercise 4

def read_student_data(filename):
    """Takes in a filename (e.g. "traffic_file.txt")
    and returns a list of counts for each line in the input file.
    """
    traffic_file = open(filename)
    all_student_counts = []
    for line in traffic_file:
        traffic_line = line.strip()
        all_student_counts.append(counts(traffic_line))
    traffic_file.close()
    return all_student_counts

def write_traffic_csv(output_filename, all_student_counts):
    """Takes in an output filename (e.g. "output.csv")
    plus the list of lists (returned by read_student_data)
    and writes each count list as a row in the csv.
    """
    with open(output_filename, "w") as trafficstrings: 
         writer = csv.writer(trafficstrings)
         writer.writerows(all_student_counts)

def print_histogram(transposed_data):
    """Takes in transposed data of read_student_data (from another function called transpose from module transpose.py)
    and prints histograms of this data.
    """
    vehicle = ["Bikes", "Car", "Lorry", "Motorbike", "Bus", "Taxi", "Van"]
    tcount = 0
    for t in transposed_data:
        hist = {}
        for count in t:
            if count in hist:
                hist[count] = hist[count] + 1
            else:
                hist[count] = 1
        print(vehicle[tcount])
        tcount = tcount + 1
        for key in sorted(hist):
            print(key, ('*' * hist[key]))


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
    bikes = percentage_bikes("BBCBLLMCCCSVSS")
    print(bikes)
    
    #question 2
    price = bridge_prices("BBCBLLMCCCSVSS")
    print(price)
    
    #question 3
    all_counts = counts("BBCBLLMCCCSVSS")
    print(all_counts)
    
    #question 4
    all_student_counts = read_student_data("trafficstrings.txt") #4a
    write_traffic_csv("output.csv", all_student_counts) #4b
    transposed_data = transpose(all_student_counts) #4c
    print_histogram(transposed_data)   #4d  


if __name__ == "__main__":
    main()