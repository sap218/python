# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 19:45:17 2017

@author: sap21
"""

from goldilocks import Goldilocks
from goldilocks.strategies import NucleotideCounterStrategy

sequence_data = {
    "bpv2": {"file": "/home/samantha/Bioinformatics/bp_v2/BP_v2.fasta.fai"}
}
g = Goldilocks(NucleotideCounterStrategy(["A", "C", "G", "T"]), sequence_data,
length="1K", stride="1K", is_faidx=True, processes=4)
g.plot("total", prop=True, tracks=["A", "C", "G", "T"])
g.query("max", track="T", limit=25)
g.export_meta()
