# @Time    : 7/19/22 7:27 AM
# @Author  : Ruizhi Cheng
# @FileName: util.py
# @Email   : rcheng4@gmu.edu
import numpy as np
import matplotlib.pyplot as plt
import argparse
import pandas as pd
import numpy as np,scipy.stats as st
RATE_bad_good = {'Extremely bad':1,'Somewhat bad':2,'Neither good nor bad':3,'Somewhat good':4,'Extremely good':5}
RATE_weak_strong ={'Much weaker':1,'Slightly weaker':2,'Medium':3,'Slightly stronger':4,'Much stronger':5}
RATE_interactive ={'Not interactive at all':1,'Slightly interactive':2,'Moderately interactive':3,'Very interactive':4,'Extremely interactive':5}
###use pandas to read the questionnaire.csv file
###extract the whole coulumn of the data
###ignore the first three line
###return a list of lists

FILENAME = 'questionnaire/questionnaire_PC.csv'
####get the head and its index of csv file
def get_head(filename):

    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[0, :]
    return x

head = get_head(FILENAME)
head_dict={}
for index,item in enumerate(head):
    ###store the head and its index in a dictionary
    head_dict[item] = index


##change head to dictionary
# head_dict = dict(zip(head,range(len(head))))
# print(head_dict)
def get_data_bad_good(filename,item):

    ###get the index of the item from head_dict
    index = head_dict[item]
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[3:, index].astype(str)
    ###change the string to integer based on RATE
    x = [RATE_bad_good[item] for item in x]
    return np.array(x)

def get_data_weak_strong(filename,item):

    ###get the index of the item from head_dict
    index = head_dict[item]
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[3:, index].astype(str)
    ###change the string to integer based on RATE
    x = [RATE_weak_strong[item] for item in x]
    return np.array(x)

def get_data_interactive(filename,item):

    ###get the index of the item from head_dict
    index = head_dict[item]
    data = pd.read_csv(filename, encoding='gbk',engine='python',header= None)
    x = data.iloc[3:, index].astype(str)
    ###change the string to integer based on RATE
    x = [RATE_interactive[item] for item in x]
    return np.array(x)

def paired_data(data1,data2):
    print('data1:',data1)
    print('data2:',data2)
    print ('normality test for data 1: ',st.normaltest(data1)[1])
    print ('normality test for data 2',st.normaltest(data2)[1])
    print ('paired t-test:',st.ttest_rel(data1, data2)[1])
    print ('Wilcoxon signed-rank test:',st.wilcoxon(data1, data2)[1])


def unpaired_data(data1,data2):
    print('data1:',data1)
    print('data2:',data2)
    print ('normality test for data 1: ',st.normaltest(data1)[1])
    print ('normality test for data 2',st.normaltest(data2)[1])
    print ('unpaired t-test:',st.ttest_ind(data1, data2)[1])
    # print ('Wilcoxon signed-rank test:',st.wilcoxon(data1, data2)[1])