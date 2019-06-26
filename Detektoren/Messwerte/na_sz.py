# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""
import numpy as np
import matplotlib.pyplot as plt
Probe = "na_sz_"
Dateinamen = ["SEP","FEP","background"]
Anzahl = np.shape(Dateinamen)
Zahlen = [0] * Anzahl[0]
m = 0.1876
E_0 = -26
m_ec=511
Literatur_FEP = 1274.5
Literatur_SEP = 511
FEP1 = 6931.29*m+E_0
FEP2 = 2863.46*m+E_0
Compton1 = FEP1*(1-1/(1+2*FEP1/(m_ec)))
Compton2 = FEP2*(1-1/(1+2*FEP2/(m_ec)))
Backscatter1 = FEP1 - Compton1
Backscatter2 = FEP2 - Compton2

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
    

plt.ylim(0.1,10**3)
plt.yscale('log')
plt.plot(x,y,".",color = "blue",label = "aktive Messwerte")  
plt.plot(x_d,y_d,".",color = "gray",label = "deaktivierte Messwerte")
plt.plot(x,f,color ="darkred", label = "Model")
for i in range(Anzahl[0]):
    plt.plot(x,Zahlen[i],label = Dateinamen[i])
plt.vlines(Literatur_FEP, ymin = 5, ymax = 300,label = "Literatur FEP 1274 keV",color = "lime")
plt.vlines(Literatur_SEP, ymin = 50, ymax = 800,label = "Literatur 511 keV",color = "lime",linestyle = "--")
plt.vlines(Compton1, ymin = 1, ymax = 100,label = "Compon-Kante FEP")
plt.vlines(Compton2, ymin = 10, ymax = 500, linestyle = "--",label = "Compon-Kante SEP")
plt.vlines(60, ymin = 20, ymax = 500,label = "Blei-Röntgen-Strahlung")
plt.vlines(Backscatter1, ymin = 20, ymax = 500,color = "red", label = "Backscatter-Kante FEP")
plt.vlines(Backscatter2, ymin = 20, ymax = 500,color = "red",linestyle = "--",label = "Backscatter-Kante SEP")

plt.legend(loc='lower left',ncol=2,prop={'size': 7})
plt.xlabel("Energie [keV]")
plt.ylabel("Zählungen")
plt.savefig(Probe + ".png")
plt.show()