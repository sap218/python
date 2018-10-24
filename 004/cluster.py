#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:41:39 2018

@author: samantha

Machine Learning Clustering
"""

import matplotlib.pyplot as plt
from sklearn import cluster #from sklearn.datasets import make_blobs
import numpy as np
import random #from random import *

'''
n_samples = 1000
X, y = make_blobs(n_samples=n_samples, centers=4)

y_pred = cluster.KMeans(n_clusters=4).fit_predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_pred)
'''

sample_A = []
sample_B = []
for c in range(50):
    sample_A.append(randint(1,1000))
    sample_B.append(randint(1,1000))
C = np.array(list(zip(sample_A, sample_B)))

D_pred = cluster.KMeans(n_clusters=3).fit_predict(C)
plt.scatter(C[:, 0], C[:, 1], c=D_pred)


'''
sample_x = [2,4,7,1,8,2,4,7,9,2,1,3,6,0,8,4,7,7,3]
sample_y = [3,6,3,2,6,1,1,5,7,3,1,2,8,4,8,5,7,6,6]
X = np.array(list(zip(sample_x, sample_y)))

y_pred = cluster.KMeans(n_clusters=3).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
#plt.savefig("clust.png")
'''
