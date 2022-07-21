# @Time    : 2/24/22 3:00 PM
# @Author  : Ruizhi Cheng
# @FileName: ovr_plot.py
# @Email   : rcheng4@gmu.edu


#This program is used to plot the metrics collected by OVR metrics tool.
#To get the metrics file, you need to enable the "Record all captured metrics to csv files" button in the OVR metrics too .
#After you quit the app, you will get the metrics file. Then you can use this program to extract and plot the metrics.
#BTW, I recommend you also enable the "Enable Persistent Overlay" button and choose "ADVANCED" in the Quick-set Enabled Stats.
#So you can observe the metrics during your experiment.
import matplotlib.pyplot as plt
from plot_paper import plot_trace

import pandas as pd
import os
import numpy as np,scipy.stats as st
# PLATFORM = '../../Worlds'
# TYPE='dis'
DATE='../0422'
TYPE = 'server'
FILENAME = '0422.csv'
file = os.path.join(DATE,TYPE,FILENAME)

def plot_trace(trace_and_label,xlabel,ylabel,low_bound,high_bound):
    x = np.arange(1, len(trace_and_label[0][0]) + 1, 1)
    fig, ax1 = plt.subplots()
    ax1.set_xlabel(xlabel, fontsize=85)
    ax1.set_ylabel(ylabel, fontsize=85)
    ##linewidth = 8 or 15
    for i in range(len(trace_and_label)):
        ax1.plot(x, trace_and_label[i][0],label=trace_and_label[i][1],linewidth = 8)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    ax1.tick_params(axis='x', labelsize = 85)
    ax1.tick_params(axis='y', labelsize = 85)
    #ax1.set_yticks(np.arange(0,0.151,0.05))
    ax1.fill_between(x, low_bound, high_bound, facecolor='blue', alpha=0.2)

    plt.grid()





    # altspace VR
    #plt.legend(fontsize=60, loc='upper center', bbox_to_anchor=(0.23, 1.15))
    plt.legend(fontsize=80, loc='upper center', bbox_to_anchor=(0.5, 1.2),ncol=2,columnspacing=0.4)
    #plt.legend(fontsize=95, loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=2)
    #plt.legend(fontsize=100, loc='best')
    plt.show()


def split_list_per_10(list):
    list_10 = []
    for i in range(0,len(list),10):
        list_10.append(list[i:i+10])
    return list_10

def get_avg_list(list):
    avg_list = []
    for i in range(len(list)):
        avg_list.append(np.mean(list[i]))
    return avg_list

def get_95_confidence_interval(list):
    confi_list = []
    for i in range(len(list)):
        confi_list.append(st.t.interval(0.95, len(list[i])-1, loc=np.mean(list[i]), scale=st.sem(list[i])))
    lower_band = []
    upper_band = []
    for i in range(len(confi_list)):
        lower_band.append(confi_list[i][0])
        upper_band.append(confi_list[i][1])
    return lower_band,upper_band

def get_cpu_total(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 1].astype(float)
    return np.array(x)


def get_memmory_utilization_percentage(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 50].astype(float)
    return np.array(x)

def get_network_rx(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 69].astype(float)
    return np.array(x)

def get_network_tx(filename):
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[1:, 71].astype(float)
    return np.array(x)

cpu_total = get_cpu_total(file)
memory_utilization_percentage = get_memmory_utilization_percentage(file)
network_rx = get_network_rx(file)
network_tx = get_network_tx(file)




###split the data per 10 data. Calculate the average and std of each group.
##########CPU

cpu_split = split_list_per_10(cpu_total)
cpu_avg = get_avg_list(cpu_split)
cpu_low,cpu_high = get_95_confidence_interval(cpu_split)
##########MEMORY

memory_split = split_list_per_10(memory_utilization_percentage)
memory_avg = get_avg_list(memory_split)
memory_low,memory_high = get_95_confidence_interval(memory_split)
cpu =[[cpu_avg,'CPU'],[memory_avg,'Memory']]

x_ticks = np.arange(1,len(cpu_avg)+1,1)
xlabel = 'Timestamp'
ylabel ='Utilization (%)'
fig, ax1 = plt.subplots()
ax1.plot(x_ticks, cpu_avg,label='CPU',linewidth=8,color = 'blue')
ax1.plot(x_ticks, memory_avg, label='Memory',linewidth=8,color='red')
x_ticks = np.arange(1,len(cpu_avg)+1,1)
# print(x_ticks)
ax1.set_ylim([0,65])
ax1.set_xticks([0,50,100,150,200])
ax1.set_yticks([10,20,30,40,50,60])
ax1.fill_between(x_ticks,cpu_low,cpu_high,facecolor='blue',alpha=0.5)
ax1.fill_between(x_ticks,memory_low,memory_high,facecolor='red',alpha=0.5)
ax1.set_xlabel(xlabel, fontsize=95)
ax1.set_ylabel(ylabel, fontsize=95)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(axis='x', labelsize=95)
ax1.tick_params(axis='y', labelsize=95)
plt.subplots_adjust(bottom=0.172)
plt.legend(fontsize=95, loc='upper center', bbox_to_anchor=(0.51, 1.2), ncol=3,columnspacing=0.5 )
plt.show()