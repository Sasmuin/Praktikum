# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 17:22:15 2019

@author: nils
"""


import numpy as np
import matplotlib.pyplot as plt
Probe = "Erz_pn_"
filename = Probe + "all.dat"
m = 0.1698
E_0 = 0
Bismut =np.array([609.3,768.4,806.2,934.1,1120.3,1238.1,1377.7])
AnzahlB = np.shape(Bismut)

Blei =np.array([53.2, 242.0, 295.2,351.9,785.9])
AnzahlBlei = np.shape(Blei)

Po214 = np.array([296, 795, 1310])
AnzahlPo214 = np.shape(Po214)

Th234 = np.array([63.3, 92.38, 92.80])
AnzahlTh234 = np.shape(Th234)

Pa234m = np.array([765,1001])
AnzahlPa234m = np.shape(Pa234m)


infile = open(filename, 'r')  # Open file for reading
line = infile.readline()      # Read first line
# Read x and y coordinates from the file and store in lists
x_d = []
y_d = []
x = []
y = []
a = []
f = []
for line in infile:
    words = line.split()      # Split line into words
    
    if (int(words[2]))==0:
        x_d.append(int(words[0]))
        y_d.append(float(words[1]))  
       
    x.append(int(words[0]))
    y.append(float(words[1]))
infile.close()

x = np.array(x)*m+E_0
x_d = np.array(x_d)*m+E_0


plt.yscale('log')
plt.plot(x,y,".",color = "blue",label = "aktive Messwerte")  
plt.plot(x_d,y_d,".",color = "gray",label = "deaktivierte Messwerte")

plt.vlines(Th234, ymin = 10, ymax = 10000,label = "Th234",color = "gold")
plt.vlines(Pa234m, ymin = 10, ymax = 10000,label = "Pa234m",color = "k")
plt.vlines(53.2, ymin = 10, ymax = 10000,label = "U234",color = "maroon")
plt.vlines(67.7, ymin = 10, ymax = 10000,label = "Th230",color = "olive")
plt.vlines(186.2, ymin = 10, ymax = 10000,label = "Ra226",color = "blue") 
plt.vlines(510, ymin = 10, ymax = 10000,label = "Rn222",color = "silver")
plt.vlines(Blei, ymin = 10, ymax = 10000,label = "Pb214",color = "tomato")
plt.vlines(Bismut, ymin = 10, ymax = 10000,label = "Bi214",color = "lime")
plt.vlines(Po214, ymin = 10, ymax = 10000,label = "Po214",color = "darkred")
plt.vlines(46.5, ymin = 10, ymax = 10000,label = "Pb210",color = "darkslategray")  
plt.vlines(803, ymin = 10, ymax = 10000,label = "Po210",color = "purple")   



plt.xlabel("Energie [keV]")
plt.ylabel("Zählungen")   
plt.legend(loc='lower left',ncol=2,prop={'size': 7})
plt.savefig(Probe + ".png")
plt.show()