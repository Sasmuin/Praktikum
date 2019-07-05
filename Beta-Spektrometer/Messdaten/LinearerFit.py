# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:36:11 2019

@author: nils
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

filename = "Untergrund.txt"
infile = open(filename, 'r')  # Open file for reading
# Read x and y coordinates from the file and store in lists
x_lin = []
y_lin = []
for line in infile:
    words = line.split()      # Split line into words
    x_lin.append(float(words[0]))
    y_lin.append(float(words[1]))
infile.close()

x_lin = np.array(x_lin)



filename = "einlesen.txt"
infile = open(filename, 'r')  # Open file for reading
# Read x and y coordinates from the file and store in lists
x = []
y = []
for line in infile:
    words = line.split()      # Split line into words
    x.append(float(words[0]))
    y.append(float(words[1]))
infile.close()

x = np.array(x)



slope, intercept, r_value, p_value, std_err = stats.linregress(x_lin, y_lin)



plt.plot(x, y, 'o', label='Messwerte')
plt.plot(x, intercept + x*slope, 'r', label='Linearer Fit durch ausgewählte Punkte')
plt.legend(prop={'size': 8})
plt.savefig("Untergrund.png")
plt.show()

y = y - intercept + x*slope
plt.plot(x, y, 'o', label='original data')
plt.xlabel("Energie [keV]")
plt.ylabel("Zählungen")
plt.savefig("Ohne_Untergrund.png")
plt.show()

Ohne_Untergrund = x_lin,y_lin



def writedat(filename, x, y, xprecision=5, yprecision=5):
    with open(filename,'w') as f:
        for a, b in zip(x, y):
            print("%.*g\t%.*g" % (xprecision, a, yprecision, b), file=f)
        
writedat("test.txt",x,y)        
        
