# @Time    : 5/15/22 2:03 AM
# @Author  : Ruizhi Cheng
# @FileName: Headset_Hubs_Zoom.py
# @Email   : rcheng4@gmu.edu

import matplotlib.pyplot as plt
import argparse
import pandas as pd
from util import get_data_bad_good,paired_data,get_data_weak_strong,get_data_interactive
import numpy as np,scipy.stats as st
First_row = 5.7
Second_row = 5.2
FILENAME = 'questionnaire/questionnaire_Headset.csv'

#####

def plot_overall(ax1,flag):
    Hubs = get_data_bad_good(FILENAME, 'Q19')
    Zoom = get_data_bad_good(FILENAME, 'Q20')
    data= [Hubs,Zoom]
    label =['Hubs','Zoom']
    print (Hubs)
    print (Zoom)
    paired_data(Hubs, Zoom)
    if flag == 'box':
        ax1.text(0.7, 1, 'Overall Experience', fontsize=90, color='red')
    elif flag == 'bar':
        ax1.text(7, Second_row, 'Overall Experience', fontsize=90, color='red')
    ax1.text(0.7,5,'P = 0.0037',fontsize=90,color='red')
    return data, label

def plot_visual(ax1,flag):
    Hubs = get_data_bad_good(FILENAME, 'Q3')
    Zoom = get_data_bad_good(FILENAME, 'Q4')
    data = [Hubs, Zoom]
    label=['Hubs', 'Zoom']
    paired_data(Hubs,Zoom)
    print (Hubs)
    print (Zoom)
    if flag == 'box':
        ax1.text(0.7, 1, 'Visual Quality', fontsize=90, color='red')
    elif flag == 'bar':
        ax1.text(7, Second_row, 'Visual Quality', fontsize=90, color='red')
    ax1.text(0.7, 5, 'P = 0.0087', fontsize=90, color='red')
    return data, label

def plot_audio(ax1,flag):
    Hubs = get_data_bad_good(FILENAME, 'Q5')
    Zoom = get_data_bad_good(FILENAME, 'Q6')
    data = [Hubs, Zoom]
    label = ['Hubs', 'Zoom']
    paired_data(Hubs, Zoom)
    if flag == 'box':
        ax1.text(0.7, 1, 'Audio Quality', fontsize=90, color='red')
    elif flag == 'bar':
        ax1.text(7, Second_row, 'Audio Quality', fontsize=90, color='red')
    ax1.text(0.7, 5, 'P = 0.0014', fontsize=90, color='red')
    return data, label


def plot_presence(ax1,flag):
    Hubs = get_data_weak_strong(FILENAME, 'Q7')
    Zoom = get_data_weak_strong(FILENAME, 'Q8')
    data = [Hubs, Zoom]
    label = ['Hubs', 'Zoom']
    print(Hubs)
    print (Zoom)
    paired_data(Hubs, Zoom)
    if flag == 'box':
        ax1.text(0.05, 1, 'Presence', fontsize=90, color='red')
    elif flag == 'bar':
        ax1.text(7, Second_row, 'Presence', fontsize=90, color='red')
    ax1.text(0.7, 5, 'P = 0.047', fontsize=90, color='red')
    return data, label

def plot_copresence(ax1,flag):
    Hubs = get_data_weak_strong(FILENAME, 'Q9')
    Zoom = get_data_weak_strong(FILENAME, 'Q10')
    data = [Hubs, Zoom]
    label = ['Hubs', 'Zoom']
    paired_data(Hubs, Zoom)
    if flag == 'box':
        ax1.text(0.05, 1, 'Co-presence', fontsize=90, color='red')
    elif flag == 'bar':
        ax1.text(7, Second_row, 'Co-presence', fontsize=90, color='red')
    ax1.text(0.7, 5, 'P = 0.00087', fontsize=90, color='red')
    return data, label

def plot_social_interaction(ax1,flag):
    Hubs = get_data_interactive(FILENAME, 'Q17')
    Zoom = get_data_interactive(FILENAME, 'Q18')
    data = [Hubs, Zoom]
    label = ['Hubs', 'Zoom']
    paired_data(Hubs, Zoom)
    print(Hubs)
    print (Zoom)
    if flag == 'box':
        ax1.text(0.05, 1, 'Social Interaction', fontsize=90, color='red')
    elif flag == 'bar':
        ax1.text(7, Second_row, 'Social Interaction', fontsize=90, color='red')
    ax1.text(0.7, 5, 'P = 0.036', fontsize=90, color='red')
    return data, label



if __name__ == '__main__':
    data,label = [],[]
    fig, ax1 = plt.subplots()
    parser = argparse.ArgumentParser()
    parser.add_argument("--o", help='overall rate', action = 'store_true')
    parser.add_argument("--v", help='video quality',action = 'store_true')
    parser.add_argument("--a", help='audio quality',action = 'store_true')
    parser.add_argument("--h", help='highly interactive', action='store_true')
    parser.add_argument("--p", help='public event', action='store_true')
    parser.add_argument("--pr", help='presence', action='store_true')
    parser.add_argument("--c", help='co-presence', action='store_true')
    parser.add_argument("--s", help='social interaction', action='store_true')
    parser.add_argument("--hp", help='harassment protection', action='store_true')
    parser.add_argument("--box", help='box plot', action='store_true')
    parser.add_argument("--bar", help='bar plot', action='store_true')
    args = parser.parse_args()
    flag = 'box' if args.box else 'bar'
    if args.o:
        data, label = plot_overall(ax1, flag)
    elif args.v:
        data, label = plot_visual(ax1, flag)
    elif args.a:
        data, label = plot_audio(ax1, flag)
    elif args.pr:
        data, label = plot_presence(ax1, flag)
    elif args.c:
        data, label = plot_copresence(ax1, flag)
    elif args.s:
        data, label = plot_social_interaction(ax1, flag)

    if args.bar:
        index = [1, 2]
        color = ['red', 'blue', 'green', 'yellow', 'orange']
        for i in range(len(data)):
            ax1.bar(index[i], height=np.mean(data[i]), yerr=np.std(data[i]), width=1.5,
                    error_kw={'elinewidth': 20, 'ecolor': 'black'}, color=color[i])
            # ax1.errorbar(label[i], np.mean(data[i]), yerr=np.std(data[i]), fmt='o')
        ax1.set_xticks(ticks=index)
        #ax1.text(7, First_row, 'All Users', fontsize=90, color='red')


    elif args.box:
        ax1.boxplot(data, labels=label, positions=[0.5, 1.5], showmeans=True, showfliers=False, widths=0.1,
                    capprops={'linewidth': '15'}, whis=(5, 95),
                    meanprops={'linewidth': '15', "marker": "o", "markersize": '30', "color": "blue"},
                    # flierprops={"markersize": '30',"markerfacecolor": "red"},
                    # whiskerprops={'linewidth':'15'},
                    medianprops={'linewidth': '15'},
                    boxprops={'linewidth': '15'}
                    )
        # ax1.set_aspect(1.5)
        ax1.text(0.05, 1.5, 'Headset Users', fontsize=90, color='red')
        #ax1.text(0.7, 1.5, 'Headset Users', fontsize=90, color='red')

    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.set_xticklabels(label, fontsize=100)
    ax1.set_ylabel('Rating', fontsize=100)
    ax1.set_yticks([1, 2, 3, 4, 5])
    ax1.set_xlim([0, 2])
    ax1.set_ylim([0.7, 5.5])
    ax1.tick_params(axis='x', labelsize=100)
    ax1.tick_params(axis='y', labelsize=100)
    plt.show()
