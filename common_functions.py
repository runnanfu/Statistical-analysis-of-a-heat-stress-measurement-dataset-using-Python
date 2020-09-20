#-- GEO1001.2020--hw01
#-- [Runnan Fu] 
#-- [5213045]

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
#common functions
#lesson A1
def mean(data):
    mean = data.mean(axis=0)
    return mean

def var(data):
    var = data.var(axis=0)
    return var
    
def std(data):
    std = data.std(axis=0)
    return std

def draw_hist(data,xlabel,nb,ax):
    fs= 10
    ax.hist(x=data,bins=nb, facecolor='lightblue', edgecolor = 'black', alpha=0.7)
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel('Frequency',fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)

def draw_fp(data, line_color, line_label, nb, ax):
    fs = 10
    y , edges, _  = ax.hist(data, bins=nb, color='w',histtype='step', linewidth=0)
    midpoint = 0.5*(edges[1:]+edges[:-1])
    ax.plot(midpoint,y, line_color, label=line_label, linewidth=1.5, alpha=1)
    ax.set_xlabel('Temperature ($^\circ$C)',fontsize=fs)
    ax.set_ylabel('Frequency',fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
    
def draw_boxplot(data,ylabel,ax):
    fs = 10
    labels = ['A', 'B', 'C', 'D', 'E']
    ax.boxplot(data,showmeans=True,patch_artist=True,labels=labels)
    ax.set_xlabel('Five separate samples',fontsize=fs)
    ax.set_ylabel(ylabel,fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
    
#lesson A2 #pdf、cdf、pmf、kde
def draw_PMF(data,xlabel,ax):
    fs = 10
    def pmf(sample):
        c = sample.value_counts()
        p = c/len(sample)
        return p
    df = pmf(data)
    df1 = df.to_frame()
    df1.reset_index(inplace=True)
    df1 = df1.astype(float)
    c = df1.sort_values(by=['index'])
    ax.bar(c.iloc[ : ,0],c.iloc[ : ,1],width=0.1, facecolor='lightblue',edgecolor='k', alpha=0.5)
    # df = pmf(data.astype(float))
    # c = df.sort_index()
    # ax.bar(c.index,c,width=0.1, color='blue', alpha=0.5)
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel('PMF',fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
    
def draw_PDF(data,xlabel,nb,ax):
    fs = 10
    y , edges, _  =ax.hist(x=data, bins=nb, density=True,color='lightblue', alpha=0.7,label = 'Histogram with Densities')
    midpoint = 0.5*(edges[1:]+edges[:-1])
    ax.plot(midpoint,y, color='blue', linewidth=1.5, alpha=0.7, label = 'PDF')
    #sns.distplot(data, bins=nb, color='b',ax=ax)
    ax.set_xlabel(xlabel, fontsize=fs)
    ax.set_ylabel('Probability Density')
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)

def draw_CDF(data,xlabel,nb,ax):
    fs = 10
    a=ax.hist(x=data, bins=nb, density=True, cumulative=True, color='lightblue', alpha=0.7)
    ax.plot(a[1][1:]-(a[1][1:]-a[1][:-1])/2,a[0], color='k')
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel('CDF',fontsize=fs)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)

def draw_KDE(data,xlabel,ax):
    fs = 10
    sns.kdeplot(data, ax=ax ,color='r',label = 'KDE')
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
    
#Lesson A3
def equal_size(data1,data2):
    return np.interp(np.linspace(0,len(data2),len(data2)),np.linspace(0,len(data1),len(data1)),data1)

def draw_scatter(data1,data2,ax,xlabel,ylabel,unit):
    fs = 10
    data1 = equal_size(data1,data2)
    ax.scatter(data1, data2, c='b',marker='.',s=1)
    ax.set_xlabel(xlabel+unit,fontsize=fs)
    ax.set_ylabel(ylabel+unit,fontsize=fs)
    ax.set_title(xlabel+' vs '+ylabel,fontsize=fs+3)
    ax.tick_params(labelsize=fs)
    ax.yaxis.grid(True)
    
#Lesson A4
def draw_interval(data, ax):
#   xquantx = ((np.quantile(data, 0.05), np.quantile(data, 0.95)))
    data_mean = data.mean()
    data_std = np.std(data, ddof = 1)
    # n=len(data)
    # data_se = data_std/np.sqrt(n)
    confi_inte = stats.norm.interval(0.95, data_mean, data_std)
    ax.axvline(confi_inte[0],color='r',linewidth = 0.5)
    ax.axvline(confi_inte[1],color='r',linewidth = 0.5)

def save_interval(data):
    data_mean = data.mean(axis=1)
    data_std = np.std(data,ddof = 1,axis=1)
    # n=data.shape[0]
    # data_se = data_std/np.sqrt(n)
    confi_inte = stats.norm.interval(0.95,  data_mean, data_std)
    return confi_inte

def creat_df(data,label):
    a=[] 
    b=[]
    for i in save_interval(data)[0]:
        a.append(i)    
    for i in save_interval(data)[1]:
        b.append(i)
    c ={label+"_lower boundary" : a,
       label+"_upper boundary" : b}
    return pd.DataFrame(c)

def hy_test(data1,data2):
    t, p_two= stats.ttest_ind(data1, data2, equal_var=False)
    return p_two
