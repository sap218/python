# -*- coding: utf-8 -*-
"""
CSM6720
@author: sap21

>> Creating a narrative with a time-line
"""

from pymongo import MongoClient   
from datetime import datetime as dt  
import numpy as np
import re

def get_ship_mates():
    """
    Searches through the MongoDB of the Aberystwyth Shipping Records, no paramters needed.
    Prints the name, year of birth, and place of birth of each ship mate.    
    Results are limited by 50 and sorted by most results first and descending.
    """
    records = db.sap21.aggregate([
        {"$match": {"mariners.year_of_birth": {"$nin": ["Blk", "blk", "blk ", "Blk "]}}},
        {"$unwind":"$mariners"},
        {"$group": {
            "_id": {
                "name": "$mariners.name",
                "year_of_birth":"$mariners.year_of_birth",
                "place_of_birth": "$mariners.place_of_birth"
            },
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 50},
        {"$skip": 2}
    ]) # gaining mariner names, birth years, and place of births in a list
    for r in records:
        print(r)
        
        
def get_year_from_field(field_data):
    """
    This function was created in order to gain date information from the records.
    Will ignore blank or unusable data.
    """
    # tries to find a year in a field of data
    if type(field_data) == dt:
        # we know we can return .year from a datetime type
        return field_data.year
    elif type(field_data) == str:
        # we have to try and find a year in a string
        # could be just a year or could be a string that has a year inside it somewhere
        match = re.search('\d{4}', field_data)
        if match:
            return int(match.group(0))
        else:
            # no valid year found?
            return None
    elif type(field_data) == int:
        # hopefully this is a year
        return field_data
    else:
        # dont know, maybe we should return field_data instead of None??
        return None
        
def get_mariner(mariner_name, year_of_birth, place_of_birth):
    """
    For efficient use: use the results of get_ship_mates()
    For example: get_mariner("John Davies", 1840, "Aberystwyth")
    This function uses get_year_from_field() in order to get dates.
    Returns the information.
    """
    records = db.sap21.find({"mariners.name": mariner_name, "mariners.year_of_birth": year_of_birth, "mariners.place_of_birth": place_of_birth})
    count = 0    
    
    this_mariner_records = []
    this_mariner_records_years = []
    for r in records:
        count += 1      
        try:
            for m in r["mariners"]:
                if m['name'] == mariner_name:                
                    record_year = get_year_from_field(m["this_ship_joining_date"])
                    if record_year:
                        m["vessel name"] = r["vessel name"] # add vessel name to mariner record for later
                        this_mariner_records.append(m)
                        this_mariner_records_years.append(record_year)
        except KeyError:
            continue
    # we can sort the list of years to sort the records for us but we are ignoring nones
    new_order = np.argsort(this_mariner_records_years)
    print("%d records found, %d records with year data returned" % (count, len(this_mariner_records_years)))
    return np.array(this_mariner_records)[new_order] # return the sorted records    
    
def print_table(records):
    """
    This function was created in order to present the data in a suitable fashion.
    """
    rows = []
    field_sizes= []
    for record in records:
        fields = [
            record["vessel name"],
            get_year_from_field(record["this_ship_joining_date"]),
            record.get("this_ship_joining_port", "Unknown"), 
            record.get("this_ship_capacity", "Unknown"),
            record.get("age", "Unknown"),
            record.get("this_ship_leaving_cause", "Unknown"),
            record.get("additional_notes", "No Notes")
        ] # this sets data to 'Unknown' if is blank
        fields = [str(x) for x in fields] # force everything to be string to make printing easier later
        rows.append(fields)
        for field_num, field_data in enumerate(fields):
            if len(field_sizes) == 0:
                # make sure field sizes have the right number of fields first
                field_sizes = [0] * len(fields)
            
            if len(field_data) > field_sizes[field_num]:
                field_sizes[field_num] = len(field_data)
        
    for row in rows:
        # add extra spaces to padd the data to make the table look nice
        for field_num, field_data in enumerate(row):
            field_data += " " * (field_sizes[field_num] - len(field_data))
            row[field_num] = field_data
        print("\t".join(row))

    

if __name__ == "__main__":
    """
    Main function demonstrating usage of functions in this script.
    """
    user = 'sap21'
    dbpath = 'nosql.dcs.aber.ac.uk/sap21'
    password = input('Enter Password...')
    connection_string = 'mongodb://'+user+':'+password+'@'+dbpath
    client = MongoClient(connection_string)
    db = client.sap21
    
    get_ship_mates() # listing all ship mates for use of next function
    
    print()
    print("Vessel Name -- Ship Join Date -- Ship Join Port -- Ship Capacity -- Age -- Ship Leaving Cause -- Notes")
    print() # using multiple 'prints' to set out data when running
    records = get_mariner("John Davies", 1840, "Aberystwyth")
    print_table(records)
    print()      
    records = get_mariner("David Davies", 1843, "Aberystwyth")
    print_table(records)
    print()
    records = get_mariner("John Jenkins", 1866, "Aberayron")
    print_table(records)    