#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:26:45 2024

@author: baff
"""

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
df = pd.read_csv('/home/baff/Downloads/guu.csv')
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
'''I=df['intensity in y'][1:52]
y=np.arange(0,25.5,0.5)


def f(x,H,a,b,sigma):
    return H + a * np.exp(-(x - b) ** 2 / (2*sigma**2))
xx = np.linspace(0,30,num=5000)
#popt, pcov = curve_fit(f,x,n)
popt, pcov = curve_fit(f,y,I,p0=[0,83.8,15,9])
fit= f(xx,*popt) 
plt.figure(figsize=(6,5))
plt.plot(xx,fit)
#plt.plot(xx,f(xx,*popt2) )
#plt.plot(x2, n2,'o', mfc='w', markersize=8, label='62.5 cm')
plt.plot(y, I,'o', mfc='w', markersize=8, label='140.5 mm')
plt.axhline(np.max(fit)/np.exp(2))
plt.xlabel('distance in y-direction (mm)')
plt.ylabel(r'Photocurrent ($\mu A$)')
'''
data=np.loadtxt('/home/baff/Downloads/guu.csv',delimiter=',')
def f(x,a,b,c,d):
    return a*np.sin(b*x+c)+d
t = data[:,0]
luma = data[:,1]
plt.figure(figsize=(10,5))
plt.plot(t[:1800]-t[0],(luma[:1800]-10)/np.max(luma-11),'o',mfc='w',markersize=8,label='data')
popt,pcov=curve_fit(f,t[:1800]-t[0],(luma[:1800]-10)/np.max(luma-11),p0=[1,np.pi,0,0])
xx=np.linspace(0,60,num=50000)
fit=f(xx,*popt)
plt.plot(xx,fit,label='fit')
plt.xlim(0,4)
plt.xlabel('Time (s)')
plt.ylabel('Intensity (AU)')
plt.legend()
plt.show()
