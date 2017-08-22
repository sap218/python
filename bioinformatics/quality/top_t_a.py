# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 19:45:17 2017

@author: sap21
"""

from goldilocks.strategies import NucleotideCounterStrategy

sequence_data = {
    "bpv2": {"file": "/home/samantha/Bioinformatics/bp_v2/BP_v2.fasta.fai"}
}
g = Goldilocks(NucleotideCounterStrategy(["A", "C", "G", "T", "N"]), sequence_data,
length="1K", stride="500", is_faidx=True, processes=4)
g.plot(prop=True, tracks=["A", "C", "G", "T", "N"])
g.query("max", track="T", limit=150)
g.export_meta()

###
'''
sequence_data = {
    "bpv1": {"file": "/home/samantha/Bioinformatics/bp_v1/BP_v1.fasta.fai"}
}
g = Goldilocks(NucleotideCounterStrategy(["A", "C", "G", "T", "N"]), sequence_data,
length="800", stride="200", is_faidx=True, processes=4)
g.plot(prop=True, tracks=["A", "C", "G", "T", "N"])
g.query("max", track="A", limit=25)
g.export_meta()
'''
###