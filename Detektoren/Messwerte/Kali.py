# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:28:27 2019

@author: nils
"""


import numpy as np
import matplotlib.pyplot as plt
Probe = "na_sz_"
Dateinamen = ["SEP","FEP"]
Anzahl = np.shape(Dateinamen)
Zahlen = [0] * Anzahl[0]

filename = Probe + "all.dat"
infile = open(filename, 'r')  # Open file for reading
line = infile.readline()      # Read first line
# Read x and y coordinates from the file and store in lists
x = []
y = []
a = []
f = []
for line in infile:
    words = line.split()      # Split line into words
           
    x.append(int(words[0]))
    y.append(float(words[1]))                  
    f.append(float(words[3])) 
infile.close()


for i in range(Anzahl[0]):
     filename = Probe + Dateinamen[i] + ".dat"
     infile = open(filename, 'r')  # Open file for reading
     line = infile.readline()      # Read first line
     # Read x and y coordinates from the file and store in lists   
     Zahlen[i] = []
     for line in infile:
         words = line.split()      # Split line into words     
         Zahlen[i].append(float(words[0]))
         
     infile.close()

plt.ylim(0.1,10**3)
plt.yscale('log')
plt.plot(x,y,".")

for i in range(Anzahl[0]):
    plt.plot(x,Zahlen[i],label = Dateinamen[i])

plt.xlabel("Channels")
plt.ylabel("Zählungen")
plt.legend()
plt.savefig("na.png")
plt.show()