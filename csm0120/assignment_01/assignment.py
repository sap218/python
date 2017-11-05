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

# exercise 2
def bridge_prices(traffic_string):
    total = 0
    price = {"B":0, "C":2, "L":5.5, "M":0.8, "S":0, "T":1, "V":3.5}
    for t in price:
        total = total + (traffic_string.count(t) * price[t])
    return "£%.2f" % total    
        
# exercise 3 
def counts(traffic_string):
    traffic_count = []
    for t in ['B', 'C', 'L', 'M', 'S', 'T', 'V']: # order changed
        traffic_count.append(traffic_string.count(t))
    return traffic_count

###############################################################
###############################################################

# exercise 4a
traffic_file = open("trafficstrings.txt")
all_student_counts = []
for line in traffic_file:
    print(line.strip())
    traffic_line = line.strip()
    print(counts(traffic_line))
    all_student_counts.append(counts(traffic_line))
traffic_file.close()
print(all_student_counts)
'''
#exercise 4b
import csv
with open("output.csv", "w") as trafficstrings: #wb
    #for line in all_student_counts:
        #trafficstrings.write(str(all_student_counts) + "\n")
        #trafficstrings.write(str(line[0])) # + "\n"
     writer = csv.writer(trafficstrings)
     writer.writerows(all_student_counts)
'''    
#exercise 4c
from transpose import transpose
transposed = (transpose(all_student_counts))
print(transposed)

#exercise 4d
#transposed[0][0]
































