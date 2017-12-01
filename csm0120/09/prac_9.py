#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:40:39 2017

@author: sap21
"""

import bs4
import requests
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
payload = {"db":"pubmed",
          "id":25136443,
          "retmode":"xml"
          }
response = requests.get(url, params=payload)
if response.status_code == 200: 
    xml_text = response.text
    #print(xml_text)
    soup = bs4.BeautifulSoup(xml_text, "xml")  
    authors = soup.find_all("Author")
    print(len(authors)) 
    title = soup.find_all("ArticleTitle")
    print(title)
    
    abstract = soup.find_all("Abstract")
    conclusion = soup.find_all('AbstractText')
    conclusion += ' Label="CONCLUSIONS"'
    print(abstract, conclusion)