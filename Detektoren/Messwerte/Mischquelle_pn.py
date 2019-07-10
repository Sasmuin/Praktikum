#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:14:14 2019

@author: nils
"""

import numpy as np
import matplotlib.pyplot as plt
Probe = "Mischquelle_pn_"
Dateinamen = ["background"]
Anzahl = np.shape(Dateinamen)
Zahlen = [0] * Anzahl[0]
m = 0.1698
E_0 = 0
m_ec=511
Literatur_FEPCO1 = 1332.5
Literatur_FEPCO2 = 1173.2
Literatur_FEP_CS = 661.6
Literatur_FEP_CS2 = 59.5


FEP2 = 7843.799*m+E_0
FEP1 = 6906.344*m+E_0
FEP3 = 3894.732762*m+E_0
FEP4 = 348.7404028*m+E_0


Compton1 = FEP1*(1-1/(1+2*FEP1/(m_ec)))
Compton2 = FEP2*(1-1/(1+2*FEP2/(m_ec)))
Compton3 = FEP3*(1-1/(1+2*FEP3/(m_ec)))
Compton4 = FEP4*(1-1/(1+2*FEP4/(m_ec)))
Backscatter1 = FEP1 - Compton1
Backscatter2 = FEP2 - Compton2
Backscatter3 = FEP3 - Compton3
Backscatter4 = FEP4 - Compton4

filename = Probe + "all.dat"
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
    f.append(float(words[3])) 
infile.close()

x = np.array(x)*m+E_0
x_d = np.array(x_d)*m+E_0



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
    

plt.ylim(0.1,5*10**4)
plt.yscale('log')
plt.plot(x,y,".",color = "blue",label = "aktive Messwerte")  
plt.plot(x_d,y_d,".",color = "gray",label = "deaktivierte Messwerte")
plt.plot(x,f,color ="darkred", label = "Model")
for i in range(Anzahl[0]):
    plt.plot(x,Zahlen[i],label = Dateinamen[i])
plt.vlines(Literatur_FEPCO1, ymin = 5, ymax = 8000,label = "Literatur FEP2 Co-60 1332.5 keV",color = "lime")
plt.vlines(Literatur_FEPCO2, ymin = 5, ymax = 8000,label = "Literatur FEP1 Co-60 1173.2 keV",color = "lime",linestyle = "--")
plt.vlines(Literatur_FEP_CS, ymin = 5, ymax = 32000,label = "Literatur FEP Cs-137 661.6 keV",color = "aqua",linestyle = "-.")
plt.vlines(46, ymin = 50, ymax = 10000,label = "Literatur FEP Am-241 59,5 keV",color = "aqua",linestyle = "--")

plt.vlines(Compton2, ymin = 10, ymax = 500,label = "Compon-Kante")
plt.vlines(Compton1, ymin = 10, ymax = 500, linestyle = "--",label = "Compon-Kante")
plt.vlines(Backscatter2, ymin = 100, ymax = 1000,color = "red",label = "Backscatter-Kante")
plt.vlines(Backscatter1, ymin = 100, ymax = 1000,color = "red", linestyle = "--",label = "Backscatter-Kante")
plt.vlines(Backscatter3, ymin = 100, ymax = 3000,color = "red", label = "Backscatter-Kante",linestyle ="--")
plt.vlines(Compton3, ymin = 20, ymax = 700,label = "Compon-Kante FEP",linestyle = "--")
plt.vlines(Backscatter4, ymin = 100, ymax = 3000,color = "red", label = "Backscatter-Kante")
plt.vlines(Compton4, ymin = 20, ymax = 700,label = "Compon-Kante")

plt.legend(loc='lower left',ncol=2,prop={'size': 7})
plt.xlabel("Energie [keV]")
plt.ylabel("Zählungen")
plt.savefig(Probe + ".png")
plt.show()