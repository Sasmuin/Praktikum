# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:34:26 2019

@author: nils
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


c = 299792458	
e = 1.602176634E-19	
me = 9.1093837015E-31
Z = 55	
alpha = 0.007299270072993


m = 1438.95017182131	
z1_0 = -604.090171821306
intercept = 0.34152456974511	
slope = -0.039697429864981

# =============================================================================
# filename = "beta.txt"
# infile = open(filename, 'r')  # Open file for reading
# # Read x and y coordinates from the file and store in lists
# x = []
# y = []
# for line in infile:
#     words = line.split()      # Split line into words
#     if (int(words[2]))==1:
#         x.append(float(words[0]))
#         y.append(float(words[1]))  
# infile.close()
# =============================================================================




filename = "test.txt"
infile = open(filename, 'r')  # Open file for reading
# Read x and y coordinates from the file and store in lists
x = []
y = []
y_err = []
for line in infile:
    words = line.split()      # Split line into words
    if (float(words[1])) > 0:
        x.append(float(words[0]))
        y.append(float(words[1]))  
        y_err.append(float(words[2]))
infile.close()



y = np.array(y)
x = np.array(x)


p = x*e/10**2

v = (1/((me/p)**2+(1/c)**2))**0.5

W = (p**2*c**2+me**2*c**4)**0.5-me*c**2
W = W*10**(-3)/e

my = Z*alpha*c/v
F = 2*np.pi*my/(1-np.exp(-2*np.pi*my))

n = np.shape(y)

eta = p


y = (y/(eta**2*F))**0.5

       
        
plt.xlim(200,500)
plt.plot(W,y,".")
