# @Time    : 7/20/22 6:03 AM
# @Author  : Ruizhi Cheng
# @FileName: corrlation_analysis.py
# @Email   : rcheng4@gmu.edu

import matplotlib.pyplot as plt
import pandas as pd
from util import get_data_bad_good,paired_data,get_data_weak_strong,get_data_interactive
import numpy as np,scipy.stats as st


headset_file = 'questionnaire/questionnaire_Headset.csv'
PC_file = 'questionnaire/questionnaire_PC.csv'

headset_hubs_overall=get_data_bad_good(headset_file, 'Q19')
headset_hubs_visual=get_data_bad_good(headset_file, 'Q3')
headset_hubs_audio=get_data_bad_good(headset_file, 'Q5')
headset_hubs_presence=get_data_weak_strong(headset_file, 'Q7')
headset_hubs_copresence=get_data_weak_strong(headset_file, 'Q9')
headset_hubs_social=get_data_interactive(headset_file, 'Q17')
headset_hubs_presence=[ 4,5,3,4,5,3,3,3,5,4,3,3,4,4,3,5,2 ]
headset_hubs_copresence=[ 3,5,5,3,5,3,4,4,5,5,5,4,5,4,3,5,2 ]
headset_hubs_social=[ 3,5,4,3,4,3,3,4,5,4,4,3,5,3,3,5,2 ]
print ('normality of headset hubs overall:',st.normaltest(headset_hubs_overall)[1])
print ('normality of headset hubs visual:',st.normaltest(headset_hubs_visual)[1])
print ('normality of headset hubs audio:',st.normaltest(headset_hubs_audio)[1])
print ('normality of headset hubs presence:',st.normaltest(headset_hubs_presence)[1])
print ('normality of headset hubs copresence:',st.normaltest(headset_hubs_copresence)[1])
print ('normality of headset hubs social:',st.normaltest(headset_hubs_social)[1])
print ('##############################################################################################')
###pearson correlation
print ('pearson correlation of visual quality and overall from headset hubs:',st.pearsonr(headset_hubs_visual, headset_hubs_overall)[1])
print ('pearson correlation of audio quality and overall from headset hubs:',st.pearsonr(headset_hubs_audio, headset_hubs_overall)[1])
print ('##############################################################################################')
print ('pearson correlation of visual quality and presence from headset hubs:',st.pearsonr(headset_hubs_visual, headset_hubs_presence)[1])
print ('pearson correlation of visual quality and copresence from headset hubs:',st.pearsonr(headset_hubs_visual, headset_hubs_copresence)[1])
print ('pearson correlation of visual quality and social interaction from headset hubs:',st.pearsonr(headset_hubs_visual, headset_hubs_social)[1])
print ('##############################################################################################')
print ('pearson correlation of audio quality and presence from headset hubs:',st.pearsonr(headset_hubs_audio, headset_hubs_presence)[1])
print ('pearson correlation of audio quality and copresence from headset hubs:',st.pearsonr(headset_hubs_audio, headset_hubs_copresence)[1])
print ('pearson correlation of audio quality and social interaction from headset hubs:',st.pearsonr(headset_hubs_audio, headset_hubs_social)[1])
##############################################################################################
###spearman correlation
print ('##############################################################################################')
print ('spearman correlation of visual quality and overall from headset hubs:',st.spearmanr(headset_hubs_visual, headset_hubs_overall)[1])
print ('spearman correlation of audio quality and overall from headset hubs:',st.spearmanr(headset_hubs_audio, headset_hubs_overall)[1])
print ('##############################################################################################')
print ('spearman correlation of visual quality and presence from headset hubs:',st.spearmanr(headset_hubs_visual, headset_hubs_presence)[1])
print ('spearman correlation of visual quality and copresence from headset hubs:',st.spearmanr(headset_hubs_visual, headset_hubs_copresence)[1])
print ('spearman correlation of visual quality and social interaction from headset hubs:',st.spearmanr(headset_hubs_visual, headset_hubs_social)[1])
print ('##############################################################################################')
print ('spearman correlation of audio quality and presence from headset hubs:',st.spearmanr(headset_hubs_audio, headset_hubs_presence)[1])
print ('spearman correlation of audio quality and copresence from headset hubs:',st.spearmanr(headset_hubs_audio, headset_hubs_copresence)[1])
print ('spearman correlation of audio quality and social interaction from headset hubs:',st.spearmanr(headset_hubs_audio, headset_hubs_social)[1])
##############################################################################################

##output the five variables in different lines
# print ('##############################################################################################')
# print ('headset hubs overall:[',",".join(map(str, headset_hubs_overall)),']')
# print ('headset hubs overall:',headset_hubs_overall)
# print ('headset hubs visual:',headset_hubs_visual)
# print ('headset hubs audio:',headset_hubs_audio)
# print ('headset hubs presence:',headset_hubs_presence)
# print ('headset hubs presence:[',",".join(map(str, headset_hubs_presence)),']')
# print ('headset hubs copresence:',headset_hubs_copresence)
# print ('headset hubs copresence:[',",".join(map(str, headset_hubs_copresence)),']')
# print ('headset hubs social:',headset_hubs_social)
# print ('headset hubs social:[',",".join(map(str, headset_hubs_social)),']')

PC_hubs_overall=get_data_bad_good(PC_file, 'Q19')
PC_hubs_visual=get_data_bad_good(PC_file, 'Q3')
PC_hubs_audio=get_data_bad_good(PC_file, 'Q5')
PC_hubs_presence=get_data_weak_strong(PC_file, 'Q7')
PC_hubs_copresence=get_data_weak_strong(PC_file, 'Q9')
PC_hubs_social=get_data_interactive(PC_file, 'Q17')

print ('normality of PC hubs overall:',st.normaltest(PC_hubs_overall)[1])
print ('normality of PC hubs visual:',st.normaltest(PC_hubs_visual)[1])
print ('normality of PC hubs audio:',st.normaltest(PC_hubs_audio)[1])
print ('normality of PC hubs presence:',st.normaltest(PC_hubs_presence)[1])
print ('normality of PC hubs copresence:',st.normaltest(PC_hubs_copresence)[1])
print ('normality of PC hubs social:',st.normaltest(PC_hubs_social)[1])
print ('##############################################################################################')
###pearson correlation
print ('pearson correlation of visual quality and overall from PC hubs:',st.pearsonr(PC_hubs_visual, PC_hubs_overall)[1])
print ('pearson correlation of audio quality and overall from PC hubs:',st.pearsonr(PC_hubs_audio, PC_hubs_overall)[1])
print ('##############################################################################################')
print ('pearson correlation of visual quality and presence from PC hubs:',st.pearsonr(PC_hubs_visual, PC_hubs_presence)[1])
print ('pearson correlation of visual quality and copresence from PC hubs:',st.pearsonr(PC_hubs_visual, PC_hubs_copresence)[1])
print ('pearson correlation of visual quality and social interaction from PC hubs:',st.pearsonr(PC_hubs_visual, PC_hubs_social)[1])
print ('##############################################################################################')
print ('pearson correlation of audio quality and presence from PC hubs:',st.pearsonr(PC_hubs_audio, PC_hubs_presence)[1])
print ('pearson correlation of audio quality and copresence from PC hubs:',st.pearsonr(PC_hubs_audio, PC_hubs_copresence)[1])
print ('pearson correlation of audio quality and social interaction from PC hubs:',st.pearsonr(PC_hubs_audio, PC_hubs_social)[1])

###spearman correlation
print ('##############################################################################################')
print ('spearman correlation of visual quality and overall from PC hubs:',st.spearmanr(PC_hubs_visual, PC_hubs_overall)[1])
print ('spearman correlation of audio quality and overall from PC hubs:',st.spearmanr(PC_hubs_audio, PC_hubs_overall)[1])
print ('##############################################################################################')
print ('spearman correlation of visual quality and presence from PC hubs:',st.spearmanr(PC_hubs_visual, PC_hubs_presence)[1])
print ('spearman correlation of visual quality and copresence from PC hubs:',st.spearmanr(PC_hubs_visual, PC_hubs_copresence)[1])
print ('spearman correlation of visual quality and social interaction from PC hubs:',st.spearmanr(PC_hubs_visual, PC_hubs_social)[1])
print ('##############################################################################################')
print ('spearman correlation of audio quality and presence from PC hubs:',st.spearmanr(PC_hubs_audio, PC_hubs_presence)[1])
print ('spearman correlation of audio quality and copresence from PC hubs:',st.spearmanr(PC_hubs_audio, PC_hubs_copresence)[1])
print ('spearman correlation of audio quality and social interaction from PC hubs:',st.spearmanr(PC_hubs_audio, PC_hubs_social)[1])
