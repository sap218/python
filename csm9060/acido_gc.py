# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:41:24 2018

@author: samantha
"""

import pysam
import matplotlib.pylab as plt

def calculate_gc(seq):
    return (seq.lower().count("g") + seq.lower().count("c")) / len(seq) * 100.0

def plot_hist(myDict, style): 
    plt.style.use(style)
    plt.hist(myDict.values(), bins=1000) 
    plt.xlabel('GC Ratio')   
    plt.ylabel('Count')
    mean_gc = (sum(myDict.values())/float(len(myDict.values())))
    plt.axvline(mean_gc, color='k')    
    plt.title('Histogram of GC for a collection of Acidobacteria sequences')
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    path = input("enter fasta file: ")
    fasta = pysam.FastaFile("/home/samantha/Dissertation/python/%s" % path) 
    
    gc = {}
    for read in fasta.references:
        gc[read] = calculate_gc(fasta.fetch(read))   
        
    max_gc = max(gc.values())
    min_gc = min(gc.values())  
    mean_gc = (sum(gc.values())/float(len(gc.values())))
    print("Min\t%f\nMax\t%f\nMean\t%f" % (min_gc, max_gc, mean_gc))

    print(plt.style.available)
    style = input("insert style you want: ")
    plt.figure(1)    
    plot_hist(gc, style)