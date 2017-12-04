'''Count k-mers in FASTA files, and compare distances between kmer profiles'''

import os
import sys
#import matplotlib.pyplot as plt

alphabet = "ACGNT"

def perms(chars, k):
    '''Make a list of all permutations of the chars, with length k'''
    if k == 1:
        return [c for c in chars]
    else:
        ps = perms(chars, k-1)
        result = []
        for c in chars:
            for p in ps:
                result.append( c+p )
        return result

def initialise_kmer_dict(chars, k):
    '''Initialise dictionary with zeros for each possible k-mer'''
    ps = perms(chars, k)
    return dict.fromkeys(ps, 0)

def distance(list1, list2):
    '''Find the distance between two lists of numbers'''
    total = 0
    for (n1,n2) in zip(list1,list2):
        total += abs(n1-n2)
    return total

def normalise(kmers):
    '''Normalise each value by dividing it by the total.'''
    total = sum (kmers.values())
    for k in kmers:
        kmers[k] = kmers[k] / total

def addcounts(filename, k, species_kmers):
    '''Add the k-mer counts for a k-mer size of k, from given file'''
    d = initialise_kmer_dict(alphabet,k)
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line.startswith(">"): # ignore header lines
                for i in range(len(line) - k + 1):
                    kmer = line[i:i+k]
                    d[kmer] += 1
        normalise(d)
        
    # Add this dictionary to the overall species_kmers dictionary
    species = filename.split('.')[0] # first part of filename
    species_kmers[species] = d

def inorder_vals(d):
    '''Return the values in an order sorted by the keys'''
    return [d[k] for k in sorted(d.keys())] 


if __name__ == "__main__":
    species_kmers = {}
    k = 1
    for filename in os.listdir():
        if filename.endswith(".fa"):
            print("Reading " + filename)
            addcounts(filename, k, species_kmers)
    print(k)
    '''for sp1 in sorted(species_kmers):
        vals1 = inorder_vals(species_kmers[sp1])
        print(vals1)
        plt.bar(range(len(vals1)), vals1)
        plt.ylim([0,0.5])
        plt.savefig(sp1+".png")
        for sp2 in sorted(species_kmers):
            vals2 = inorder_vals(species_kmers[sp2])
            print("%.8f %s %s" % (distance(vals1,vals2),sp1,sp2))
            '''