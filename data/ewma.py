# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:53:40 2020

@author: NielCansino
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_dist(raw, filtered, span):
    for i in range(data.shape[1]):
        column_name = raw.columns[i]
        plt.plot(raw.iloc[:, i], color = 'orange', linestyle='dashed', label=column_name+"_raw")
        plt.plot(filtered.iloc[:, i], color='green', label=column_name+"_filtered")
    plt.title('RSSI (raw and EWMA-filtered data) with span='+str(span))
    plt.xlabel('time (s)')
    plt.ylabel('RSSI (dBm)')
    plt.show()  
    
def plot_rssi_to_dist(b, a, calc_distance):
    plt.title('RSSI vs. Distance w/ fit coefficients a='+str(a)+' and b='+str(b))
    r=np.arange(-100,40) # arbitrary RSSI
    plt.xlabel('distance (m)')
    plt.ylabel('RSSI (dB)')
    plt.plot(r, calc_distance(r))
    plt.show()

if __name__ == "__main__":
    # import data
    filename = "raw/2020-09-20.csv"
    data = pd.read_csv(filename, index_col=0)
     
    # take EWMA with span=10 samples
    span = 10
    fwd_filtered = pd.DataFrame.ewm(data,span=span).mean() # take EWMA in fwd direction
    
    # plot
    plot_dist(data, fwd_filtered, span)
    
    # Curve Fitting
    # log10 d = MP/(10N) - RSSI / (10N)
    # or log10(distance) = A + B*RSSI
    distance = np.array(pd.to_numeric(data.columns))
    rssi = np.array(data.mean(axis=0))
    [b, a] = np.polyfit(rssi, np.log10(distance), 1, w=np.sqrt(distance))
    
    
    def calc_distance(rssi): return 10**(a + b*rssi)
    # Try to draw 