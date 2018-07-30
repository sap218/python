# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:50:13 2018

@author: samantha
"""

import pysam
import collections
import matplotlib.pyplot as plt

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
    plt.title('Histogram of ACGT for a collection of Acidobacteria sequences')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    path = input("enter fasta file: ") # acido_reads_2018-07-28_22-28-17.fa
    fasta = pysam.FastaFile("/home/samantha/Dissertation/python/%s" % path) 

    '''
    reads = []
    for read in fasta.references:
        reads.append(fasta.fetch(read))
    max_read = len(max(reads, key=len))
    min_read = len(min(reads, key=len))
    print("Read Lengths\tMin: %i\tMax: %i" % (min_read, max_read))
    readlen = len(reads[1])
    print("Read Length of a random read:\t%i" % (readlen))
    results = []    
    x = 0
    for letter in reads:
        result = collections.Counter(reads[x])
        x = x + 1
        results.append(result)
    print("ACGT count of a random read: ", results[1])
    '''
    
    at = {}
    gc = {}
    for read in fasta.references:
        at[read] = calculate_at(fasta.fetch(read))  
        gc[read] = calculate_gc(fasta.fetch(read))
    '''
    max_at = max(at.values())
    min_at = min(at.values())  
    mean_at = (sum(at.values())/float(len(at.values())))
    print("AT\nMin\t%f\nMax\t%f\nMean\t%f" % (min_at, max_at, mean_at))
    max_gc = max(gc.values())
    min_gc = min(gc.values())  
    mean_gc = (sum(gc.values())/float(len(gc.values())))
    print("GC\nMin\t%f\nMax\t%f\nMean\t%f" % (min_gc, max_gc, mean_gc))
    '''
    print(plt.style.available)
    style = input("insert style you want: ")
    x = 1
    plt.figure(x)    
    plot_hist(at, style)
    plot_hist(gc, style)