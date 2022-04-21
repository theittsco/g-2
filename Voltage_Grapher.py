# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 12:44:00 2018

@author: Scott
"""
import pandas as pd
import matplotlib.pyplot as plt

file = 'Induction Coil Magnetometry.xlsx'

data = pd.ExcelFile(file)
df = pd.read_excel(data, '3D-Printed_New')
dfy = pd.read_excel(data, 'Short-Cable-Coil')

#Getting rid of the 32-avg column. It clutters.
df_dropped = df.drop(['Accquire Mode'], axis='columns')
dfy2 = dfy.drop(dfy.index[77:])
#Getting Rid of the labels of the radii and stuff. It adds clutter.
df_final = df_dropped.drop(df.index[77:])

#Help me I'm lost. Where art thou, my Resonance frequency?

y_max_loc = df_final['Ratio Measured/Linear Voltage'].argmax()
x_res = df_final[' Frequency (Hz)'].loc[y_max_loc]
y_res = df_final['Ratio Measured/Linear Voltage'].max()
note_x_res = 'Resonance at ' + str(x_res) +' Hz'


#I LOVE summaries. Fun fact.
print(df_final)
print(df_final.describe())

#BECAUSE WHO DOESN'T LOVE SEXY GRAPHS?

plt.figure(1)
plt.plot(df_final[' Frequency (Hz)'],df_final['Phase'])
plt.ylabel('Phase')
plt.xlabel('Frequency/Hz')
plt.grid()
plt.title('Phase')
plt.show()

#Comparison graphs
plt.figure(2)
plt.plot(df_final[' Frequency (Hz)'], df_final['Measured Voltage (V)'], '.-r', label='New Wire')
plt.plot(df_final[' Frequency (Hz)'],df_final['Predicted Voltage (V)'], '.-b', label='Predicted')
#plt.plot(dfy2[' Frequency (Hz)'], dfy2['Induced Voltage (V)'], '.-g',label='Short')
plt.title('Comparison Expected Versus Actual Voltage')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Voltage (V)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid()
plt.show()

#Histograms are important.
plt.subplot(1, 3, 1)
plt.hist(df_final['Driving Voltage (V)'], normed=True, color='blue')
plt.title('Driving Voltage Peak to Peak')
plt.xlabel('Voltage (V)')
plt.subplot(1, 3, 2)
plt.hist(df_final['B_Applied (T)'], color='red')
plt.title('Applied Magnetic Field')
plt.xlabel('Magnetic Field (T)')
plt.subplot(1,3,3)
plt.hist(df_final['Ratio Measured/Predicted Voltage'],bins=7,color='green')
plt.xlabel('Ratio')
plt.title('Ratio Actual/Expected Voltage')
plt.tight_layout()
plt.show()

pd.set_option('display.precision', 5)
