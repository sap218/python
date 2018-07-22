# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 14:19:49 2018
@author: samantha
"""
import requests
import bs4
from bs4 import BeautifulSoup
import csv

def insert_csv(file):
    dict_seqid_taxon = {}
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t') # tab
        for row in reader:
            if row["taxon"] not in dict_seqid_taxon:
                dict_seqid_taxon[row["taxon"]] = { "reads": [] }     
            dict_seqid_taxon[row["taxon"]]["reads"].append(row["seqid"])
    return dict_seqid_taxon # above swaps over the columns and avoids the duplicates

def search(taxon):
    url = "https://www.ncbi.nlm.nih.gov/taxonomy/?"
    payload = {"term":taxon}
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        return response.text
    else:
        return None

def print_html(html_doc):
    soup = bs4.BeautifulSoup(html_doc, "html.parser") # making it beautiful
    return soup
    
def soup_tag(soup):
    results = {}    
    try:
        tag = soup.find("p", {"class": "title"}).contents[0].contents[0] # searching for the name
        results["species"] = tag
    except (NameError, TypeError, IndexError):
        print("bad response from NCBI")
    try:
        tag = soup.find("div", {"class": "rprt", "class": "supp"}).contents[0].contents[0] # description
        results["description"] = tag
    except (NameError, TypeError, IndexError):
        print("bad response from NCBI")
    return results

def percentage(part, whole):
    return 100 * float(part)/float(whole)

if __name__ == "__main__":
    taxon_map = insert_csv("/home/samantha/Dissertation/python/kaiju_allC_seqid_taxon.csv")    
    #taxon_map = insert_csv("/home/samantha/Dissertation/python/kaiju_allC_seqid_taxon_head.csv")
    #taxon_map = insert_csv("/home/samantha/Dissertation/python/kaiju_allC_seqid_taxon_head20.csv") # insert csv
    for s in taxon_map:
        response = search(s) # using function search to read through the taxons
    
        if response is None:
            print("bad response from NCBI")
        else:
            soup = print_html(response)
        #html_content = soup.prettify() # prettify the html before tagging
        tag = soup_tag(soup)
        taxon_map[s].update(tag) # extending the taxon map dictionary
        #print(taxon_map[s]) # one by one
        #print(taxon_map)
        
    list_of_reads = []
    acid_ratio = 0
    nn_ratio = len(taxon_map)   
    for a in taxon_map:
        if "Acido" in taxon_map[a]["species"] or "Acido" in taxon_map[a]["description"]:
            print(taxon_map[a])
            acid_ratio = acid_ratio + 1
            list_of_reads.extend(taxon_map[a]["reads"])
    print("acido coverage of file", percentage(acid_ratio, nn_ratio))
    
    with open("newfilereads.txt", "w") as output:
        for item in list_of_reads:
            output.write("%s\n" % item)