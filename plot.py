# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 08:51:26 2017

@author: zx_pe
"""
import matplotlib.pyplot as plt
import seaborn as sns
#%% Plot Helper

def boxplotter(data, x=None, y=None, size = (8,8), save=False, filename=None, **kwargs):
    plt.subplots(figsize=size)
    s = sns.boxplot(x=x,y=y,data=data, **kwargs)
    if save:
        f = s.get_figure()
        f.savefig(filename)
    return s

def distplotter(data, size = (8,8), save=False, filename=None, **kwargs):
    plt.subplots(figsize=size)
    s = sns.distplot(data, **kwargs)
    if save:
        f = s.get_figure()
        f.savefig(filename)
    return s

def countplotter(x, data, size = (8,8), save=False, filename=None, **kwargs):
    plt.subplots(figsize=size)
    s = sns.countplot(x=x,data=data, **kwargs)
    if save:
        f = s.get_figure()
        f.savefig(filename)
    return s
#%% Boxplots
    
boxplotter(x="School", y="2015_Result", data=data, showmeans=True)
boxplotter(data=data[['2014_Result','2015_Result']], size = (4,8))
boxplotter(data=data['PCHI'], size = (2,8))

#%% Distribution Plots

[distplotter(data[score]) for score in scores]

#%% Count Plots
countplotter(x='PSLE_Result',data=data)
[countplotter(x=cat,data=data) for cat in catVar]

#%% Comparison Boxplots

[boxplotter(x=cat, y="PSLE_Result", data=data, showmeans=True) for cat in catVar]
[boxplotter(x='Programme', y=score, data=data, showmeans=True) for score in scores]
boxplotter(x='att_pass', y = 'PSLE_Result', data = att_merge, showmeans=True, size = (4,8))

#%% Improvement plots

data['Improvement'] = data['2015_Result'] - data['2014_Result'] #Create Improvement variable
[boxplotter(x=cat, y="Improvement", data=data, showmeans=True) for cat in catVar]

#%% Pairwise Plot
plt.subplots(figsize=(8, 8))
sns.pairplot(data[['PCHI','2014_Result','2015_Result','PSLE_Result']], hue ='PSLE_Result')
#%% Correlation heatmap
plt.subplots(figsize=(8, 8))
sns.heatmap(data[['PCHI','2014_Result','2015_Result','PSLE_Result']].corr(), annot=True)
