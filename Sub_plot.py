# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 22:52:52 2022

@author: Suresh BASNET
"""

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
m1=5     # Slope of the line
m2=3.5
c=-1   # Intercept of the line 
x=np.linspace(0,10,15)   # Make the list of x
y1=m1*x+c             # Equation of straight line.
y2=m2*x+c

plt.figure(figsize = [10,6]) # Control the figure size

plt.subplot(2, 2, 1)
plt.plot(x,y1,color='red',linestyle='-.', linewidth = 1.5, 
         marker='o', markerfacecolor='b', markersize=5,label='For slope m1')
plt.plot(x,y2,color='black',linestyle=':', linewidth = 1.5, 
         marker='*', markerfacecolor='b', markersize=7,label='For slope m2')

plt.rcParams.update({'font.family':'Times New Roman'})
plt.legend()
plt.legend(loc='upper left',prop = {'size': 14})

plt.xlim(-2,12)
plt.ylim(-10,60)
#plt.xlabel('$x$-value', fontsize=16,color='red')
plt.ylabel('$y$-value', fontsize=14,color='black')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.text(-5, 56,'( a )',fontsize=14)  #===Give the figure number for subplot
#=============Add minor ticks
plt.minorticks_on()
plt.tick_params(which='major', length=6)
plt.tick_params(which='minor', length=3)
#================================================
#plot 2:
m1=10     # Slope of the line
m2=5
c=-5   # Intercept of the line 
x=np.linspace(0,10,15)   # Make the list of x
y1=m1*x+c             # Equation of straight line.
y2=m2*x+c

plt.subplot(2, 2, 2)
plt.plot(x,y1,color='red',linestyle='-.', linewidth = 1.5, 
         marker='o', markerfacecolor='b', markersize=5,label='For slope m1')
plt.plot(x,y2,color='black',linestyle=':', linewidth = 1.5, 
         marker='*', markerfacecolor='b', markersize=7,label='For slope m2')

#plt.rcParams.update({'font.family':'Times New Roman'})
#plt.legend()
#plt.legend(loc='upper left',prop = {'size': 14})

plt.xlim(-2,12)
plt.ylim(-10,60)
#plt.xlabel('$x$-value', fontsize=16,color='red')
#plt.ylabel('$y$-value', fontsize=14,color='black')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.text(-1.5, 50,'( b )',fontsize=14)
#=============Add minor ticks
plt.minorticks_on()
plt.tick_params(which='major', length=6)
plt.tick_params(which='minor', length=3)

#======================Plot 3
#plot 2:
m1=10     # Slope of the line
m2=5
c=-5   # Intercept of the line 
x=np.linspace(0,10,15)   # Make the list of x
y1=m1*x+c             # Equation of straight line.
y2=m2*x+c

plt.subplot(2, 2, 3)
plt.plot(x,y1,color='red',linestyle='-.', linewidth = 1.5, 
         marker='o', markerfacecolor='b', markersize=5,label='For slope m1')
plt.plot(x,y2,color='black',linestyle=':', linewidth = 1.5, 
         marker='*', markerfacecolor='b', markersize=7,label='For slope m2')

plt.rcParams.update({'font.family':'Times New Roman'})
#plt.legend()
#plt.legend(loc='upper left',prop = {'size': 14})

plt.xlim(-2,12)
plt.ylim(-10,60)
plt.xlabel('$x$-value', fontsize=16,color='red')
plt.ylabel('$y$-value', fontsize=14,color='black')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.text(-1.5, 50,'( c )',fontsize=14)
#=============Add minor ticks
plt.minorticks_on()
plt.tick_params(which='major', length=6)
plt.tick_params(which='minor', length=3)

#===========================Plot 4
m1=10     # Slope of the line
m2=5
c=-5   # Intercept of the line 
x=np.linspace(0,10,15)   # Make the list of x
y1=m1*x+c             # Equation of straight line.
y2=m2*x+c

plt.subplot(2, 2, 4)
plt.plot(x,y1,color='red',linestyle='-.', linewidth = 1.5, 
         marker='o', markerfacecolor='b', markersize=5,label='For slope m1')
plt.plot(x,y2,color='black',linestyle=':', linewidth = 1.5, 
         marker='*', markerfacecolor='b', markersize=7,label='For slope m2')

plt.rcParams.update({'font.family':'Times New Roman'})
#plt.legend()
#plt.legend(loc='upper left',prop = {'size': 14})

plt.xlim(-2,12)
plt.ylim(-10,60)
plt.xlabel('$x$-value', fontsize=16,color='red')
#plt.ylabel('$y$-value', fontsize=14,color='black')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.text(-1.5, 50,'( d )',fontsize=14)
#=============Add minor ticks
plt.minorticks_on()
plt.tick_params(which='major', length=6)
plt.tick_params(which='minor', length=3)
#================================================

plt.savefig('sub_figure.png', dpi=300,bbox_inches='tight')             # Save the obtained plot
plt.show()