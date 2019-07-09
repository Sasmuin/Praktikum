# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:36:11 2019

@author: nils
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

m = 1274.893502331
err_m = 275.353173423193	
z1_0 = -503.778177447552
err_z1_0 = 409.734320537812

	

c = 299792458	
e = 1.602176634E-19	
me = 9.1093837015E-31
Z = 55	
alpha = 0.007299270072993

intercept = 0.34152456974511	
err_intercept = 0.00570897207488
slope = -0.039697429864981
err_slope = 0.00651507467445

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
def writedat(filename, x, y,y_err, xprecision=6, yprecision=5,y_errprecision=7):
    with open(filename,'w') as f:
        for a, b,c in zip(x, y,y_err):
            print("%.*g\t%.*g\t%.*g" % (xprecision, a, yprecision, b,y_errprecision,c), file=f)

def fit(x,a,b): 
     return a*x+b

#Zeug einlesen
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


#Linearer Fit um Untergrund Z0 zu entfernen
popt,pcov=curve_fit(fit,x_lin,y_lin) 
a=popt[0]; err_a=np.sqrt(pcov[0,0])
b=popt[1]; err_b=np.sqrt(pcov[1,1])
perr = np.sqrt(np.diag(pcov))


#plot von ursprünglichen Daten + Fit
plt.figure(1)                
plt.subplot(111)
plt.plot(x, y, 'o', label='Messwerte')
plt.plot(x, b + x*a, 'r', label="Linearer Fit durch ausgewählte Punkte \n mit m=({:2.0f}".format(a)  +"±{:2.0f}".format(err_a) + ")(1/mA)\n und  b=({:4.0f}".format(b) +"±{:3.0f}".format(err_b)+")")
plt.legend(prop={'size': 8})
plt.xlabel("Stromstärke (mA)")
plt.ylabel("Zählungen")
plt.savefig("Untergrund.png")
plt.show()

#ursprüngliche Daten ohne Untergrund Z0 und plot
y = y - b - x*a
y_err = (err_b**2+(err_a*x)**2)**0.5
plt.errorbar(x, y,y_err,ls="none",marker=".",label = "Messwerte") 
plt.xlabel("Stromstärke (mA)")
plt.ylabel("Zählungen")
plt.legend()
plt.savefig("Ohne_Untergrund.png")
plt.show()

#Speichert Daten ohne Untergrund z0
writedat("test.txt",x,y,y_err)


#y Fehler nach Entfernung von Untergrund Z0
y_err = (err_b**2+(err_a*x)**2)**0.5


#plot für Untergrund Z1
plt.ylim(0,10000)
plt.plot(x, y, '.', label='original data')
plt.plot(x, z1_0 + x*m, 'r', label="Linearer Fit durch ausgewählte Punkte \n mit m=({:4.0f}".format(m)  +"±{:3.0f}".format(err_m) + ")(1/mA)\n und  b=({:3.0f}".format(z1_0) +"±{:3.0f}".format(err_z1_0)+")")
plt.xlabel("Stromstärke (mA)")
plt.ylabel("Zählungen")
plt.legend()
plt.savefig("Z1.png")
plt.show()

#Entfernt Untergrund Z1
y = y - x*m+z1_0
y_err = (y_err**2+err_m*x+err_z1_0)**0.5
x = x*intercept + slope
x_err = (err_intercept**2+(err_slope*x)**2)**0.5








writedat("z1.txt",x,y,y_err)        
        


filename = "z1.txt"
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

v = p/me

W = (p**2*c**2+me**2*c**4)**0.5-me*c**2
W = W*10**(-3)/e

my = Z*alpha*c/v
F = 2*np.pi*my/(1-np.exp(-2*np.pi*my))

n = np.shape(y)[0]

eta = p

xdata = []
ydata = []
error = []
WurzelN = (y/(eta**2*F))**0.5
y_err = y_err/(2*WurzelN*eta**2*F)

 
    
for i in range(n):
    if W[i] < 500 and W[i] > 400:
        xdata.append(W[i])
        ydata.append(WurzelN[i])
        error.append(y_err[i])
        
  
popt,pcov=curve_fit(fit,xdata,ydata,sigma=error,p0=(-1.0*10**(20),1.0*10**23)) 
a=popt[0]; err_a=np.sqrt(pcov[0,0])
b=popt[1]; err_b=np.sqrt(pcov[1,1])
perr = np.sqrt(np.diag(pcov))

plt.xlim(250,500)
xdata = np.array(xdata)
plt.plot(W, b + W*a, 'r', label="Linearer Fit durch ausgewählte Punkte \n mit m=({:3.1e}".format(a)  +"±{:2.0e}".format(err_a) + ")s/(kg m keV)\n und  b=({:4.2e}".format(b) +"±{:3.0e}".format(err_b)+")s/(kg m)")
plt.errorbar(W, WurzelN,y_err, ls="none",marker=".") 
plt.gca().set_ylabel(r'$\sqrt{\frac{N}{p^{2}F}}$')
plt.xlabel("Energie(keV)")
plt.legend()
plt.savefig("Kurie.png")
plt.show


E_0 = -b/a
err_E_0 = E_0*((err_b/b)**2+(err_a/a)**2)**0.5
print(E_0,err_E_0)
 
# =============================================================================
# plt.xlim(200,500)
# plt.plot(W,WurzelN,".")
# =============================================================================


