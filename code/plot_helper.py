#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     :2022/1/6 7:14 PM
# @Author   :Ruizhi Cheng

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np,scipy.stats as st
import os
ROOT = '../..'

dash_line = {0:'-',1:'--',2:'-.'}
####create a figure
#[[trace,label],[trace,label],[trace,label]]
def plot_trace(trace_and_label,xlabel,ylabel):
    x = np.arange(1, len(trace_and_label[0][0]) + 1, 1)
    fig, ax1 = plt.subplots()
    ax1.set_xlabel(xlabel, fontsize=85)
    ax1.set_ylabel(ylabel, fontsize=85)
    ##linewidth = 8 or 15
    for i in range(len(trace_and_label)):
        ax1.plot(x, trace_and_label[i][0],label=trace_and_label[i][1],linewidth = 8)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ### 120 or 80
    ax1.tick_params(axis='x', labelsize = 85)
    ax1.tick_params(axis='y', labelsize = 85)
    #ax1.set_yticks(np.arange(0,0.151,0.05))

    ###TCP uplink
    ###latency
    ax1.set_xlim([0.1, 310])
    ax1.set_ylim([0,2.1])
    ax1.set_yticks([0, 0.3, 0.5, 0.7, 1.0, 1.5])
    ax1.set_xticks([60, 120, 180, 240, 300])
    ax1.text(20, 1.35, '5s', fontsize=80, color='red')
    ax1.text(70, 1.35, '10s', fontsize=80, color='red')
    ax1.text(130, 1.35, '15s', fontsize=80, color='red')
    ax1.text(185, 1.35, '100%', fontsize=80, color='red')
    ax1.text(260, 1.35, 'N', fontsize=80, color='red')


    plt.grid()
    
    #plt.legend(fontsize=60, loc='upper center', bbox_to_anchor=(0.23, 1.15))
    plt.legend(fontsize=80, loc='upper center', bbox_to_anchor=(0.5, 1.2),ncol=2,columnspacing=0.4)
    #plt.legend(fontsize=95, loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2)
    #plt.legend(fontsize=100, loc='best')
    plt.show()

def get_col(filename,col_index):
    data = pd.read_csv(filename, encoding='gbk', engine='python', header=None)
    x = data.iloc[1:, col_index].astype(float)
    return np.array(x)

