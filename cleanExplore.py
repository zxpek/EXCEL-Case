# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 00:57:40 2017

@author: zx_pe
"""
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
os.chdir("D:\OneDrive\GitHub\EXCEL-Case")

results = pd.read_csv("Data\\results_info_20160324.csv")
attendance = pd.read_csv("Data\\attendance_records_20160324.csv").fillna('N')
demographic = pd.read_csv("Data\\demographic_info_20160324.csv")

data = demographic.merge(results, on = ['NRIC','School','Programme'])
    
#.merge(attendance, on = ['NRIC','School','Programme'], how = "left")
#%%
#Plot missing values
missing = data.isnull().sum(axis=0).reset_index()
missing.columns = ['column_name', 'missing_count']
missing = missing.sort_values(by='missing_count', ascending=False)
fig, ax = plt.subplots(figsize=(8, 8))

g = sns.barplot(x='column_name',y='missing_count',data=missing,palette='Blues_d')
g.set_xticklabels(missing.column_name.values, rotation='30')
g.set(xlabel = '', ylabel = "Number of Missing Values")
g.set_title('Number of Missing Values per Column')
#%%
#Fill missing values
data['PCHI'].fillna(np.mean(data['PCHI']),inplace=True)
data['2015_Result'].fillna(np.mean(data['2015_Result']),inplace=True)
#data['PSLE_Result'].fillna('NA',inplace=True)

data = data.astype({'School':'category', 'Programme':'category', 'Gender':'category','Flat_Type':'category'})    
data['PSLE_Result'] = data['PSLE_Result'].astype('category', ordered=True)
data['PSLE_Result'] = data['PSLE_Result'].cat.reorder_categories(['U','E','D','C','B','A','A*'])
data.to_csv("Data\\clean.csv")
#%%
#Distribution Plots
sns.distplot(data['PCHI'],kde=False,fit=stats.gamma)
sns.distplot(data['2015_Result'],kde=False,fit=stats.gamma)
sns.distplot(data['2014_Result'],kde=False,fit=stats.gamma)

#%%
#Pairwise Plot
sns.pairplot(data, hue ='PSLE_Result')
#plt.title("Important variables correlation map", fontsize=15)
#plt.show()
#%%
fig, ax = plt.subplots(figsize=(8, 8))
sns.boxplot(x="School", y="PCHI", data=data).set_xticklabels(rotation=30);
sns.boxplot(x="Flat_Type", y="PCHI", data=data);
sns.boxplot(x="Programme", y="PCHI", data=data);
sns.boxplot(x="PSLE_Result", y="PCHI", data = data)
#%%
fig, ax = plt.subplots(figsize=(8, 8))
sns.boxplot(x="School", y="2015_Result", data=data)
sns.boxplot(x="Flat_Type", y="2015_Result", data=data);
sns.boxplot(x="Programme", y="2015_Result", data=data);
sns.boxplot(x="PSLE_Result", y="2015_Result", data = data)
#%%
fig, ax = plt.subplots(figsize=(8, 8))
sns.boxplot(x="School", y="2014_Result", data=data).set_xticklabels(rotation=30);
sns.boxplot(x="Flat_Type", y="2014_Result", data=data);
sns.boxplot(x="Programme", y="2014_Result", data=data);
sns.boxplot(x="PSLE_Result", y="2014_Result", data = data)
#%%
#Stacked Bar
sns.barplot(x=)