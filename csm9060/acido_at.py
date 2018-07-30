# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:50:13 2018

@author: samantha
"""

import pysam
import collections

def calculate_at(seq):
    return (seq.lower().count("a") + seq.lower().count("t")) / len(seq) * 100.0

if __name__ == "__main__":
    path = input("enter fasta file: ") # acido_reads_2018-07-28_22-28-17.fa
    fasta = pysam.FastaFile("/home/samantha/Dissertation/python/%s" % path) 

    reads = []
    for read in fasta.references:
        reads.append(fasta.fetch(read))
    results = []    
    for letter in reads:
        result = collections.Counter(reads[0])
        results.append(result)
    
    at = {}
    for read in fasta.references:
        at[read] = calculate_at(fasta.fetch(read))
    for key, value in at.items():
        if value > 55:
            print("%s\t%.2f" % (key, value))