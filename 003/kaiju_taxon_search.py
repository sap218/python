# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 14:19:49 2018
@author: samantha
"""

import requests
import bs4
from bs4 import BeautifulSoup

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
    
    tag = soup.find("p", {"class": "title"})
    try:
        for t in tag:
                results.append(tag)
    except (NameError, TypeError):
        print("bad response from NCBI")
    tag = soup.find("div", {"class": "rprt", "class": "supp"})
    try:
        for t in tag:
                results.append(tag)
    except (NameError, TypeError):
        print("bad response from NCBI")

    return results


if __name__ == "__main__":
    response = search("1797182")
    if response is None:
        print("bad response from NCBI")
    else:
        soup = print_html(response)
    #html_content = soup.prettify()  
    #print(html_content)
     
    tag = soup_tag(soup)
    for t in tag:
        tag.append(str(t))
        #print(str(t))