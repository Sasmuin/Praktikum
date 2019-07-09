#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:45:45 2019

@author: nils
"""

import numpy as np
import matplotlib.pyplot as plt

def Ellipse(a,b,alpha,Farbe,Legende):
    X = np.linspace(-a,a,300)
    F1 = b/a * np.sqrt(a**2-X**2)
    F2 = -b/a * np.sqrt(a**2-X**2)
    F1_neu = X*np.sin(alpha) + F1*np.cos(alpha)
    F2_neu = X*np.sin(alpha) + F2*np.cos(alpha)
    X1 = X*np.cos(alpha) - F1*np.sin(alpha)
    X2 = X*np.cos(alpha) - F2*np.sin(alpha)
    plt.plot(X1,F1_neu,Farbe,label = Legende)
    plt.plot(X2,F2_neu,Farbe)
    return 
    

alpha1 = np.pi*50/180
a1= 1
b1 = 0.014

alpha2 = np.pi*103/180
a2 = 0.869
b2 = 0.186

alpha3 = np.pi*123/180
a3 = 0.98
b3 = 0.028
Ellipse(a1,b1,alpha1,"b","Grauwert:0")
Ellipse(a2,b2,alpha2,"green","Grauwert:150")
Ellipse(a3,b3,alpha3,"red","Grauwert:250")
plt.axis("equal")
plt.xlabel("Intensität in x-Richtung[W]")
plt.ylabel("Intensität in y-Richtung[W]")
plt.legend()
plt.savefig("Bericht/Ellipse.png")
plt.show()