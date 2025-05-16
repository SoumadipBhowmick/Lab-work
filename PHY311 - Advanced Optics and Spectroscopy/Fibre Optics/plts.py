# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import scienceplots
plt.rcParams.update({'font.size': 18})
plt.style.use(['science','no-latex'])
#df = pd.read_csv('/home/baff/Downloads/guu.txt')
df = pd.read_csv('/media/baff/New\ Volume/Lab-work/PHY311 - Advanced Optics and Spectroscopy/Gaussian Beam/Untitled spreadsheet - 282.2 mm.csv')
'''x = [0,
26.3307,
53.928,
81.2936,
119.6811,
132.4136,
158.4011]

x2=[0,
38.9344,
71.0896,
123.5871,
173.6019,
222.4936]'''
#n = np.arange(0,7)
#n2 = np.arange(0,6)
#y=df['Y (mm)']
I=df['intensity in y'][1:]
y=np.arange(0,26,0.5)


def f(x,H,a,b,sigma):
    return H + a * np.exp(-(x - b) ** 2 / (2*sigma**2))
xx = np.linspace(0,50,num=5000)
#popt, pcov = curve_fit(f,x,n)
popt, pcov = curve_fit(f,y,I,p0=[0,10,19,9])
fit= f(xx,*popt) 
plt.figure(figsize=(6,5))
plt.plot(xx,fit)
#plt.plot(xx,f(xx,*popt2) )
#plt.plot(x2, n2,'o', mfc='w', markersize=8, label='62.5 cm')
plt.plot(y, I,'o', mfc='w', markersize=8, label='282.2 mm')
plt.axhline(np.max(fit)/np.exp(2))
plt.xlabel('distance in y-direction (mm)')
plt.ylabel(r'Photocurrent ($\mu A$)')
plt.legend()
plt.show()
