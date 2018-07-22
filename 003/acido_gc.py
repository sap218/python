# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:41:24 2018

@author: samantha
"""

import pysam
import matplotlib.pylab as plt

def calculate_gc(seq):
    return (seq.lower().count("g") + seq.lower().count("c")) / len(seq) * 100.0

def plot(myDict):
    plt.bar(gc.keys(), gc.values())
    #plt.xlabel('seq id')
    plt.xticks(rotation=90)
    plt.ylabel('percentage')
    plt.ylim(0,100)
    plt.title('plot of GC content of seq ids')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    acido_reads = {}
    #fasta = pysam.FastaFile("/home/samantha/Dissertation/python/acido.fasta")
    fasta = pysam.FastaFile("/home/samantha/Dissertation/python/acido_200.fasta")  
    
    gc = {}
    for read in fasta.references:
        gc[read] = calculate_gc(fasta.fetch(read))    
    #print(gc)
    plot(gc)    