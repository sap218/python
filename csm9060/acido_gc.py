# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:41:24 2018

@author: samantha
"""

import pysam
import matplotlib.pylab as plt

def calculate_gc(seq):
    return (seq.lower().count("g") + seq.lower().count("c")) / len(seq) * 100.0

def plot_hist(myDict): 
    plt.hist(myDict.values()) 
    plt.xlabel('gc ratio')    
    #plt.xticks(rotation=90)
    plt.ylabel('num of sequences')
    plt.xlim(25,75)
    plt.title('histogram count of of GC ratio for a collection of seq ids')
    plt.grid(True)
    plt.show()
    
def plot_seqGC(myDict):
    name = str(myDict.keys())
    plt.bar(myDict.keys(), myDict.values())     
    plt.xlabel('seq id')   
    plt.xticks(rotation=90)
    plt.ylabel('ratio')
    plt.ylim(25,75)
    plt.title('plot for seq ids GC ratio for a certain portion')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    acido_reads = {}
    #fasta = pysam.FastaFile("/home/samantha/Dissertation/python/acido_200.fasta")
    fasta = pysam.FastaFile("/home/samantha/Dissertation/python/newfilereads.fa")
    
    gc = {}
    for read in fasta.references:
        gc[read] = calculate_gc(fasta.fetch(read))    
    #print(gc)  
    
    max_gc = max(gc.values())
    min_gc = min(gc.values())  
    print(max_gc, min_gc)
    
    
    dict_less_30 = {}
    dict_30_40 = {}
    dict_40_50 = {}
    dict_50_60 = {}
    dict_60_70 = {}
    dict_more_70 = {}
    
    for key,val in gc.items():
        if val < 30: 
            dict_less_30[key] = val
        elif val < 40 and val > 30:
            dict_30_40[key] = val
        elif val < 50 and val > 40:
            dict_40_50[key] = val
        elif val < 60 and val > 50:
            dict_50_60[key] = val
        elif val < 70 and val > 60:
            dict_60_70[key] = val
        elif val > 70:
            dict_more_70[key] = val
    
    #plt.figure(1)
    #plot_hist(gc)
    #plt.figure(2)
    #plot_seqGC(dict_30_40)
    
    list_of_gc = [dict_less_30, dict_30_40, dict_40_50, dict_50_60, dict_60_70, dict_more_70]    
    
    x = 1
    for i, gc_dict in enumerate(list_of_gc):
        #plt.figure(i)
        plt.figure(x)
        x = x + 1
        plot_seqGC(gc_dict)