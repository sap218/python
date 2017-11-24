#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 11:11:37 2017

@author: sap21
"""

import aviary
import owl

ceri = owl.Owl("tawny owl", "twit twoo", "tree", 123)
dyfi = owl.Owl("barn owl", "shriek", "barn", wing_span=5.332)
cati = owl.Owl("tawny owl", "hoohoo", ring_number=345)

#cosy_home can be borth
cosy_home = aviary.Aviary()
cosy_home.add(ceri)
cosy_home.add(dyfi)
cosy_home.addtwice(cati)
print(cosy_home.count())
print(cosy_home.get_dict())
cosy_home.describe()