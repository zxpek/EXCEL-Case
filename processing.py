# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 08:59:48 2017

@author: zx_pe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


results = pd.read_csv("Data\\results_info_20160324.csv")
attendance = pd.read_csv("Data\\attendance_records_20160324.csv").fillna('N')
demographic = pd.read_csv("Data\\demographic_info_20160324.csv")

data = demographic.merge(results, on = ['NRIC','School','Programme'])

catVar = ['School','Programme','Gender','Flat_Type']
scores = ['PSLE_Result','2015_Result','2014_Result']
#%% Plot missing values
missing = data.isnull().sum(axis=0).reset_index()
missing.columns = ['column_name', 'missing_count']
missing = missing.sort_values(by='missing_count', ascending=False)
fig, ax = plt.subplots(figsize=(8, 8))

g = sns.barplot(x='column_name',y='missing_count',data=missing,palette='Blues_d')
g.set_xticklabels(missing.column_name.values, rotation='30')
g.set(xlabel = '', ylabel = "Number of Missing Values")
g.set_title('Number of Missing Values per Column')
#%% Fill missing values
data['PCHI'].fillna(np.mean(data['PCHI']),inplace=True)
data['2015_Result'].fillna(np.mean(data['2015_Result']),inplace=True)
#data['PSLE_Result'].fillna('NA',inplace=True)

data = data.astype({'School':'category', 'Programme':'category', 'Gender':'category','Flat_Type':'category'})    
data['PSLE_Result'] = data['PSLE_Result'].astype('category', ordered=True)
data['PSLE_Result'] = data['PSLE_Result'].cat.reorder_categories(['U','E','D','C','B','A','A*'])
data.to_csv("Data\\clean.csv", index=False)

#%% One-hot processing and Convert PSLE to numerical
catVar = ['School','Programme','Gender','Flat_Type']
scores = ['PSLE_Result','2015_Result','2014_Result']

#Convert to numerical
data['PSLE_Result'] = data['PSLE_Result'].replace(['U','E','D','C','B','A','A*'],[10,27,42,54.5,67,82.5,95.5])
data['PSLE_Result'].fillna(np.nanmean(data['PSLE_Result']), inplace=True)

#OneHot processing
data_OneHot = pd.concat([data,pd.get_dummies(data[catVar])], axis = 1).drop(catVar, axis = 1)
data_OneHotInvertible = data_OneHot.drop([j+"_"+data[j].unique()[-1] for j in catVar], axis = 1) #Make matrix invertible (no linearly dependent rows)

dataX = data_OneHotInvertible.drop(['NRIC','PSLE_Result','2015_Result'], axis = 1)
dataY = data_OneHotInvertible['PSLE_Result']