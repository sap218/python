#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:58:34 2017

@author: sap21
"""

# hansard.py
'''
into = '.,?()!:-"' # [".",",","?"]
out = "         "
punctuation = str.maketrans(into,out)

speech = open("PMQs_181017.txt")
for line in speech:
    line.translate(punctuation)
speech.close()
'''

# exercise 1
def remove_punctuation(text):
    into = '.,?()!:-"' # [".",",","?"]
    out = "         "
    punctuation = str.maketrans(into,out)

    for line in text:
        string = line.translate(punctuation)
    return string
    