# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:39:07 2023

@author: André
"""

import numpy as np
import matplotlib.pyplot as plot

vetor1 = np.random.beta(22.5,2.5,1000000)
vetor2 = np.random.beta(15.5,3.5,1000000)

d = vetor1-vetor2

plot.hist(d,100)

print(np.quantile(d, 0.025), np.quantile(d, 0.975))

"""
OR = []
for i in range(len(vetor1)):
    
    OR += [ (vetor1[i] / (1-vetor1[i])) / (vetor2[i] / (1-vetor2[i])) ]
    

plot.hist(OR,1000)
print(np.quantile(OR, 0.025), np.quantile(OR, 0.975))
"""



