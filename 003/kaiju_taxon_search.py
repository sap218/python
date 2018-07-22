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
    with open(file, newline='') as csvfile:
        #reader = csv.reader(csvfile, delimiter=' ')
        reader = csv.DictReader(file)
...     for row in reader:
...         print(row['seqid'], row['taxon'])

def search(taxon):
    url = "https://www.ncbi.nlm.nih.gov/taxonomy/?"
    payload = {"term":taxon}
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        return response.text
    else:
        return None

def print_html(html_doc):
    soup = bs4.BeautifulSoup(html_doc, "html.parser")
    return soup
    
def soup_tag(soup):
    results = []    
    try:
        tag = soup.find("p", {"class": "title"}).contents[0].contents[0]
        results.append(tag)
    except (NameError, TypeError, IndexError):
        print("bad response from NCBI")
    try:
        tag = soup.find("div", {"class": "rprt", "class": "supp"}).contents[0].contents[0]
        results.append(tag)
    except (NameError, TypeError, IndexError):
        print("bad response from NCBI")
    return results


if __name__ == "__main__":
    insert_csv("/home/samantha/Dissertation/kaiju_allC_seqid_taxon.csv")
    
    response = search("1797182")
    if response is None:
        print("bad response from NCBI")
    else:
        soup = print_html(response)
    #html_content = soup.prettify()  
    #print(html_content)
    tag = soup_tag(soup)
    for t in tag:
        print(t)