# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:50:13 2018

@author: samantha
"""

import pysam
import collections
import matplotlib.pyplot as plt
from time import gmtime, strftime

############################

def list_of_sequences(fasta): # list of sequences, e.g. ['AGCT', 'TAGC']
    reads = []
    for read in fasta.references:
        reads.append(fasta.fetch(read))
    return reads
def counting_acgt(list): # getting ACGT count for each sequence
    results = []
    x = 0
    for letter in list:
        result = collections.Counter(list[x])
        x = x + 1
        results.append(result)
    return results

def calculate_at(seq):
    return (seq.lower().count("a") + seq.lower().count("t")) / len(seq) * 100.0
def calculate_gc(seq):
    return (seq.lower().count("g") + seq.lower().count("c")) / len(seq) * 100.0

def plot_hist(myDict, style): 
    plt.style.use(style)
    plt.hist(myDict.values(), bins=1000) 
    plt.xlabel('Ratio')   
    plt.ylabel('Count')
    
    meanDict = (sum(myDict.values())/float(len(myDict.values())))
    plt.axvline(x=meanDict, color='k')
    plt.text(x=meanDict, y=meanDict, s=str("%.2f" % meanDict))
    
    plt.title('Histogram of ACGT for a collection of\nAcidobacteria sequences')
    plt.grid(True)
    #plt.show()
    plt.savefig('acgt_%s.png' % time_stamp)

###############################

if __name__ == "__main__":    
    time_stamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())     
    path = input("enter fasta file: ") # acido_reads_2018-07-28_22-28-17.fa
    fasta = pysam.FastaFile("/home/samantha/Dissertation/python/%s" % path) 

    reads = list_of_sequences(fasta)   
    max_read = len(max(reads, key=len))
    min_read = len(min(reads, key=len))
    print("Read Lengths\tMin: %i\tMax: %i" % (min_read, max_read))
    #results = counting_acgt(reads)
    
    at = {}
    gc = {}
    for read in fasta.references:
        at[read] = calculate_at(fasta.fetch(read))  
        gc[read] = calculate_gc(fasta.fetch(read))
    max_at = max(at.values())
    min_at = min(at.values())  
    print("AT\tMin: %f\tMax: %f" % (min_at, max_at))
    max_gc = max(gc.values())
    min_gc = min(gc.values())  
    print("GC\tMin: %f\tMax: %f" % (min_gc, max_gc))

    print(plt.style.available)
    style = input("insert style you want: ")
    x = 1
    plt.figure(x)    
    plot_hist(at, style)
    plot_hist(gc, style)
    