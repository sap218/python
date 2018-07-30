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
    
def plot_seqGC(myDict):
    max_gc = max(myDict.values())
    min_gc = min(myDict.values()) 
    plt.bar(myDict.keys(), myDict.values())     
    plt.xlabel('Seq ID')   
    plt.xticks(rotation=90)
    plt.ylabel('Ratio')
    plt.ylim(min_gc,max_gc)
    plt.title('GC ratio of a specific portion of Sequence IDs')
    plt.grid(True)
    plt.show()
    
#######
    
if __name__ == "__main__":
    path = input("enter fasta file: ") # acido_reads_2018-07-28_22-28-17.fa
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
    x = 1
    plt.figure(x)    
    plot_hist(gc, style)
    
    #########
    '''
    ans = input("continue? (y/n) ")
    if ans == "y":
        dict_less_50 = {}
        dict_50_55 = {}
        dict_55_60 = {}
        dict_60_65 = {}
        dict_more_65 = {}
        
        for key,val in gc.items():
            if val < 50: 
                dict_less_50[key] = val
            elif val < 55 and val > 50:
                dict_50_55[key] = val
            elif val < 60 and val > 55:
                dict_55_60[key] = val
            elif val < 65 and val > 60:
                dict_60_65[key] = val
            elif val > 65:
                dict_more_65[key] = val
        
        list_of_gc = [dict_less_50, dict_50_55, dict_55_60, dict_60_65, dict_more_65]    
        for i, gc_dict in enumerate(list_of_gc):
            #plt.figure(i)
            x = x + 1
            plt.figure(x)
            #plot_seqGC(gc_dict) # dictionaries are large :( 
            plot_hist(gc_dict, "ggplot")
    else:
        pass
    '''