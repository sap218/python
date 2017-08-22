# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 20:58:03 2017

@author: sap21
"""

from goldilocks import Goldilocks
from goldilocks.strategies import GCRatioStrategy

### SCATTER
sequence_data = {
    "bpv2": {"file": "/home/samantha/Bioinformatics/bp_v2/BP_v2.fasta.fai"}
}
g = Goldilocks(GCRatioStrategy(), sequence_data, length="1K", stride="1K", is_faidx=True)
g.plot(title="GC Content over bpv2 Chr1-3")

#####################

sequence_data = {
    "bpv2": {"file": "/home/samantha/Bioinformatics/bp_v2/BP_v2.fasta.fai"}
}
g = Goldilocks(GCRatioStrategy(), sequence_data, length="1K", stride="25", is_faidx=True)
g.plot(chrom=1, title="GC Content over Chr1")

##################### POTENTIAL BUG

sequence_data = {
    "bpv2": {"file": "/home/samantha/Bioinformatics/bp_v2/BP_v2.fasta.fai"}
}
g = Goldilocks(GCRatioStrategy(), sequence_data, length="1K", stride="25", is_faidx=True)
g.plot(title="GC Content")