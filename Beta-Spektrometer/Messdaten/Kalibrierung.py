#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:20:57 2019

@author: nils
"""
import matplotlib.pyplot as plt


filename = "Kalibrierung.dat"
infile = open(filename, 'r')  # Open file for reading
# Read x and y coordinates from the file and store in lists
x = []
y = []
Model = []
for line in infile:
    words = line.split()      # Split line into words
    if (float(words[2])) == 1:
        x.append(float(words[0]))
        y.append(float(words[1]))  
        Model.append(float(words[3]))
infile.close()

plt.plot(x,y,".",label = "Messwerte")
plt.plot(x,Model,label = "Gauß Fits")
plt.xlabel("Stromstärke (mA)")
plt.ylabel("Zählungen")
plt.legend()
plt.savefig("Kalibrierung.png")
plt.show()