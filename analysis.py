# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:30:57 2017

@author: zx_pe
"""

import numpy as np
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import scipy.stats as stats
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
os.chdir("D:\OneDrive\GitHub\EXCEL-Case")
data = pd.read_csv("Data\\clean.csv").drop('NRIC',axis=1)

#%% One-hot processing and Convert PSLE to numerical
catVar = ['School','Programme','Gender','Flat_Type'] #,'PSLE_Result'
data['PSLE_Result'] = data['PSLE_Result'].replace(['U','E','D','C','B','A','A*'],[10,27,42,54.5,67,82.5,95.5])
data['PSLE_Result'].fillna(np.nanmean(data['PSLE_Result']), inplace=True)
data_OneHot = pd.concat([data,pd.get_dummies(data[catVar])], axis = 1).drop(catVar, axis = 1)

dataX = data_OneHot.drop(['PSLE_Result'], axis = 1)
dataY = data_OneHot['PSLE_Result']

#%% PCA
drops = [i for i in catVar]
dropCols = [j+"_"+i for j in drops for i in data[j].unique()]

data_scaled = scale(data_OneHot.drop(dropCols, axis = 1))
data_scaled = scale(data_OneHot)
pca = PCA(n_components = 2)
pca.fit(data_scaled)
print(pca.explained_variance_ratio_)
pcaTransform = pca.transform(data_scaled)
data['PCA1'], data['PCA2'] = pcaTransform[:,0], pcaTransform[:,1]
sns.lmplot('PCA1','PCA2',data = data, fit_reg = False, hue = 'Gender')
sns.lmplot('PCA1','PCA2',data = data, fit_reg = False)
sorted(zipped, key=lambda x: x[1])

[i for i in sorted(zip(pca.components_[0],data_OneHot.columns), key = lambda x: abs(x[0]))]
[i for i in sorted(zip(pca.components_[1],data_OneHot.columns), key = lambda x: abs(x[0]))]
#%% OLS Regression
lm = LinearRegression()
lm.fit(dataX,dataY) #Remove multicollinear rows

lm = sm.OLS(dataY, dataX).fit()
lm.summary()
#%% ANOVA
EXCEL = data_OneHot.loc[data['Programme'] == 'EXCEL' ,:]
PASS = data_OneHot.loc[data['Programme'] == 'PASS' ,:]

scores = ['PSLE_Result','2015_Result','2014_Result']
EXCEL_scores = EXCEL.loc[: , scores]
PASS_scores = PASS.loc[: ,scores]

f = stats.f_oneway(EXCEL,PASS)
[(str(i)) for i in zip(EXCEL.columns[1:],f[1])]
#%% Test difference in scores between groups
means = (EXCEL_scores.apply(np.mean, axis = 0), PASS_scores.apply(np.mean, axis = 0))
mean_ttests = [stats.ttest_ind(EXCEL_scores[i],PASS_scores[i])[1] for i in scores]

print(means)
print(mean_ttests)
#%% Test difference in scores over the year for both groups
improv_ttests = [stats.ttest_ind(df['2015_Result'], df['2014_Result'])[1] for df in [EXCEL, PASS]]
print(improv_ttests)

