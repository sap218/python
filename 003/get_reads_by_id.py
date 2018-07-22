# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 17:41:24 2018

@author: samantha
"""

import sys                                                                                                        
import pysam                                                                                                      
                                                                                                                  
reads = set([x.strip() for x in open(sys.argv[1]).readlines()])                                                   
fasta = pysam.FastaFile(sys.argv[2])                                                                              
                                                                                                                  
for r in reads:                                                                                                   
    seq = fasta.fetch(reference=r)                                                                                
    print (">%s\n%s" % (r, seq))