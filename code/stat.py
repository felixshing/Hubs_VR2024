# @Time    : 7/18/22 8:31 PM
# @Author  : Ruizhi Cheng
# @FileName: stat.py
# @Email   : rcheng4@gmu.edu


import numpy as np
import matplotlib.pyplot as plt
import numpy as np,scipy.stats as st
'''
PC_overall = [1*[3],12*[4],7*[5]]
PC_overall=sum(PC_overall,[])
Headset_overall = [1*[1], 2 * [2], 4 * [3], 7 * [4], 3 * [5]]
Headset_overall = sum(Headset_overall, [])

print(st.normaltest(PC_overall)[1])
print(st.normaltest(Headset_overall)[1])
print(st.ttest_ind(PC_overall,Headset_overall)[1])

Visual
PC_visual = [2 * [3], 11 * [4], 7 * [5]]
PC_visual = sum(PC_visual, [])
Headset = [2 * [1], 2 * [2], 3 * [3], 8 * [4], 2 * [5]]
    Headset = sum(Headset, [])

print (st.normaltest(PC_visual)[1])
print (st.normaltest(Headset_visual)[1])
print (st.ttest_ind(PC_visual,Headset_visual)[1])


Audio
PC = [1*[2],3 * [3], 9 * [4], 7 * [5]]
PC = sum(PC, [])
Headset = [2 * [1], 3 * [2], 3 * [3], 6 * [4], 2 * [5]]
Headset = sum(Headset, [])

Presence
PC = [1 * [1], 4 * [3], 12 * [4], 3 * [5]]
PC = sum(PC, [])
Headset = [7 * [3], 5 * [4], 4 * [5]]
Headset = sum(Headset, [])

Co-presence
PC = [1 * [1], 1 * [2], 6 * [3], 6 * [4], 6 * [5]]
PC = sum(PC, [])
Headset = [4 * [3], 4 * [4], 8 * [5]]
Headset = sum(Headset, [])

Social Interaction
PC = [2 * [2], 6* [3], 9 * [4], 3 * [5]]
PC = sum(PC, [])
Headset = [7 * [3], 6 * [4], 3 * [5]]
Headset = sum(Headset, [])


print (st.normaltest(PC)[1])
print (st.normaltest(Headset)[1])
print (st.ttest_ind(PC,Headset)[1])
print (st.mannwhitneyu(PC,Headset)[1])
'''


'''
overall
Hubs = [1 * [3], 12 * [4], 7 * [5]]
Hubs = sum(Hubs, [])
Zoom = [6 * [3], 5 * [4], 9 * [5]]
Zoom = sum(Zoom, [])
visual
Hubs = [1*[2],1 * [3], 11 * [4], 7 * [5]]
Hubs = sum(Hubs, [])
Zoom = [1*[2],3 * [3], 8 * [4], 8 * [5]]
Zoom = sum(Zoom, [])
'''

Hubs = [2 * [3], 9 * [4], 7 * [5],2 * [4] ]
Hubs = sum(Hubs, [])
Zoom = [2 * [3], 9 * [4], 9 * [5]]
Zoom = sum(Zoom, [])
# Hubs = [5,4,5,4,4,5,5,3,4,4,4,5,5,4,4,4,4,5,4,4]
# Zoom = [3,4,5,3,3,5,5,5,4,5,3,4,5,3,4,4,5,5,3,5]
print (Hubs)
print (Zoom)
#
# print (st.normaltest(Hubs)[1])
# print (st.normaltest(Zoom)[1])
test1=[3,5]
test2=[5,3]
print (st.ttest_rel(test1,test2)[1])
# #print (st.wilcoxon(Hubs,Zoom,zero_method = 'pratt')[1])
# PC = [2 * [2], 6* [3], 9 * [4], 3 * [5]]
# PC = sum(PC, [])
# Headset = [7 * [3], 7 * [4], 3 * [5]]
# Headset = sum(Headset, [])
#
# print (st.normaltest(PC)[1])
# print (st.normaltest(Headset)[1])
# print (st.ttest_ind(PC,Headset)[1])