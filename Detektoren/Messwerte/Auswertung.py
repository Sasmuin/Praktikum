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
    

plt.ylim(0.1,10**5)
plt.yscale('log')
plt.plot(x,y,".",color = "blue",label = "aktive Messwerte")  
plt.plot(x_d,y_d,".",color = "gray",label = "deaktivierte Messwerte")
for i in range(Anzahl[0]):
    plt.plot(x,Zahlen[i],label = Dateinamen[i])
plt.plot(x,f, label = "Model")
plt.vlines(1050, ymin = 1, ymax = 100, linestyle = "-.",label = "Compon-Kante 1274keV")
plt.vlines(300, ymin = 10, ymax = 500, linestyle = "--",label = "Compon-Kante 511keV")
plt.vlines(60, ymin = 10, ymax = 500,label = "Blei-Röntgen")


plt.legend(loc='upper center',ncol=2)
plt.xlabel("Energie")
plt.ylabel("Zählungen")
plt.savefig(Probe + ".png")
plt.show()