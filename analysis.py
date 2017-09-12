# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 00:30:57 2017

@author: zx_pe
"""
from sklearn.linear_model import LinearRegression
import scipy.stats as stats
import statsmodels.api as sm

# PCA
##drops = ['School','Programme']
##dropCols = [j+"_"+i for j in drops for i in data[j].unique()[:-1]]
##data_scaled = scale(data_OneHotInvertible.drop(dropCols, axis = 1))
##columns = data_OneHotInvertible.drop(dropCols, axis = 1).columns
#
#data_scaled = scale(data_OneHotInvertible)
#columns = data_OneHotInvertible.columns
#
#pca = PCA(n_components = 2)
#pca.fit(data_scaled)
#print(pca.explained_variance_ratio_)
#pcaTransform = pca.transform(data_scaled)
#data['PCA1'], data['PCA2'] = pcaTransform[:,0], pcaTransform[:,1]
#sns.lmplot('PCA1','PCA2',data = data, fit_reg = False, hue = 'Gender')
#
#[i for i in sorted(zip(pca.components_[0],columns), key = lambda x: abs(x[0]))]
#[i for i in sorted(zip(pca.components_[1],columns), key = lambda x: abs(x[0]))]


#%% Test difference in scores between groups (Two-tailed)
EXCEL = data_OneHotInvertible.loc[data['Programme'] == 'EXCEL' ,:]
PASS = data_OneHotInvertible.loc[data['Programme'] == 'PASS' ,:]

EXCEL_scores = EXCEL.loc[: , scores]
PASS_scores = PASS.loc[: ,scores]

means = (EXCEL_scores.apply(np.mean, axis = 0), PASS_scores.apply(np.mean, axis = 0))
mean_ttests = [stats.ttest_ind(EXCEL_scores[i],PASS_scores[i])[1] for i in scores]

print(means)
print(mean_ttests)

#%% OLS Regression
lm = LinearRegression()
lm.fit(dataX,dataY) #Remove multicollinear rows

lm = sm.OLS(dataY, dataX).fit()
lm.summary()

#%% Chi-Square

def chisq(cat):
    subset = data.loc[data['Programme'] == 'EXCEL' , cat]
    excel_count = subset.value_counts()
    pop_count = (data[cat].value_counts()/data.shape[0])*subset.shape[0]

    chsq = stats.chisquare(excel_count,pop_count)
    return (chsq[1])

[(cat,chisq(cat)) for cat in catVar]

#%% Test difference in scores over the year for both groups
improv_ttests = [stats.ttest_ind(df['2015_Result'], df['2014_Result'])[1] for df in [EXCEL, PASS]]
print(improv_ttests)

#%% Test difference for OWNED and RENTAL students
#Owned = data.loc[(data['Flat_Type'] == 'OWNED') & (data['Programme'] == 'EXCEL') ,'Improvement']
#Rental = data.loc[(data['Flat_Type'] == 'RENTAL') & (data['Programme'] == 'EXCEL')  ,'Improvement']
#
#flat_ttests = stats.ttest_ind(Owned,Rental)
#print(flat_ttests)

#%% Test difference for schools
kiasu = data.loc[(data['School'] == 'Kiasu Parents Primary School') & (data['Programme'] == 'EXCEL') ,'Improvement']
normal = data.loc[(data['School'] == 'Normal Primary School') & (data['Programme'] == 'EXCEL')  ,'Improvement']
playhard = data.loc[(data['School'] == 'Play Hard Primary School') & (data['Programme'] == 'EXCEL') ,'Improvement']

school_ftest = stats.f_oneway(kiasu, normal, playhard)
print(school_ftest)