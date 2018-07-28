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
    plt.hist(myDict.values(), bins=100) 
    plt.xlabel('gc ratio')   
    plt.ylabel('num of sequences')
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
    path = input("enter fasta file ")
    fasta = pysam.FastaFile("/home/samantha/Dissertation/python/%s" % path) 
    
    #fasta = pysam.FastaFile("/home/samantha/Dissertation/python/newfilereads.fa") 
    #fasta = pysam.FastaFile("/home/samantha/Dissertation/python/ncbi-genomes/full_genomes/allgenomes.fna")
    #fasta = pysam.FastaFile("/home/samantha/Dissertation/python/ncbi-genomes/full_genomes/sub_6_GCF_001618865.1_ASM161886v1_genomic.fna")
    #fasta = pysam.FastaFile("/home/samantha/Dissertation/python/ncbi-genomes/sub_8_genomic.fna")
    gc = {}
    for read in fasta.references:
        gc[read] = calculate_gc(fasta.fetch(read))   
        
    max_gc = max(gc.values())
    min_gc = min(gc.values())  
    mean_gc = (sum(gc.values())/float(len(gc.values())))
    print("Min %f \nMax %f \nMean %f" % (min_gc, max_gc, mean_gc))

    plt.style.use('ggplot')
    plt.figure(1)    
    plot_hist(gc)
    #plt.figure(2)
    #plot_seqGC(gc)  
    
    '''
    # this part only for 'all' stuff
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
    
    plt.figure(3)
    plot_seqGC(dict_more_70)
    '''
    ''' 
    list_of_gc = [dict_less_30, dict_30_40, dict_40_50, dict_50_60, dict_60_70, dict_more_70]    
    x = 1
    for i, gc_dict in enumerate(list_of_gc):
        #plt.figure(i)
        plt.figure(x)
        x = x + 1
        plot_seqGC(gc_dict)
    '''