# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 14:19:49 2018
@author: samantha
"""

import csv                                                                                                        
import pysam  

def insert_csv(file):
    dict_seqid_taxon = {}
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t') # tab
        for row in reader:
            if row["taxon"] not in dict_seqid_taxon:
                dict_seqid_taxon[row["taxon"]] = { "reads": [] }     
            dict_seqid_taxon[row["taxon"]]["reads"].append(row["seqid"])
    return dict_seqid_taxon # above swaps over the columns and avoids the duplicates

def load_taxondump(path):
    taxons = {}
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t') # tab
        for row in reader:
            if "acidobacteria" in row[2].lower() and "scientific name" in row[6]:
                #print(row[0], row[2])
                taxons[row[0]] = row[2]
        return taxons

#####

def percentage(part, whole):
    return 100 * float(part)/float(whole)

#####

if __name__ == "__main__":
    taxon_read_map = insert_csv("/home/samantha/Dissertation/python/kaiju_allC_seqid_taxon.csv")    
    #taxon_read_map = insert_csv("/home/samantha/Dissertation/python/kaiju_allC_seqid_taxon_head.csv")
    taxons = load_taxondump("/home/samantha/Dissertation/python/taxdump/names.dmp")  # ftp://ftp.ncbi.nih.gov/pub/taxonomy/
    
    has_taxon = 0
    total_reads = 0
    numrec = 0
    to_remove = []
    acido_reads = []
    for taxon_id in taxon_read_map:
        try:
            taxon_read_map[taxon_id]["scientific_name"] = taxons[taxon_id] # try to find taxon id for acidobacteria
            has_taxon += len(taxon_read_map[taxon_id]["reads"])
            acido_reads.extend(taxon_read_map[taxon_id]["reads"])
        except KeyError:
            to_remove.append(taxon_id)            
            #taxon_read_map[taxon_id]["scientific_name"] = None
        numrec += 1
        total_reads += len(taxon_read_map[taxon_id]["reads"])
        print("record", numrec)
    for taxon_id in to_remove:
        #pass        
        del taxon_read_map[taxon_id]
    #print(taxon_read_map)
    print("acido coverage of file", percentage(has_taxon, total_reads))
    

    acido_reads = set(acido_reads)
                                                     
    fasta = pysam.FastaFile("/home/samantha/Dissertation/all.fa")
    with open("newfilereads.fa", "w") as output:
        for r in acido_reads:                                                                                                   
            seq = fasta.fetch(reference=r)                                                                                
            #print (">%s\n%s" % (r, seq))
            output.write(">%s\n%s\n" % (r, seq))
    