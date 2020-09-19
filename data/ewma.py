# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:53:40 2020

@author: NielCansino
"""

import matplotlib.pyplot as plt
import pandas as pd

def plot_dist(raw, filtered, span):
    for i in range(data.shape[1]):
        column_name = raw.columns[i]
        plt.plot(raw.iloc[:, i], color = 'orange', linestyle='dashed', label=column_name+"_raw")
        plt.plot(filtered.iloc[:, i], color='green', label=column_name+"_filtered")
    plt.title('RSSI (raw and EWMA-filtered data) with span='+str(span))
    plt.xlabel('time (s)')
    plt.ylabel('RSSI (dBm)')
    plt.show()    

if __name__ == "__main__":
    # import data
    filename = "raw/2019-09-13.csv"
    data = pd.read_csv(filename, index_col=0)
     
    # take EWMA with span=10 samples
    span = 10
    fwd_filtered = pd.DataFrame.ewm(data,span=span).mean() # take EWMA in fwd direction
    
    # plot
    plot_dist(data, fwd_filtered, span)