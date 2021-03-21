#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:11:35 2021

@author: darshayblount
"""
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/darshayblount/Documents/1 MSDA/DataViz/netflix_titles.csv')

#netflix.head(3)

#Data Preprocessing
for i in df.columns:
    null_rate = df[i].isna().sum() / len(df) * 100 
    if null_rate > 0 :
        print("{} null rate: {}%".format(i,round(null_rate,2)))
        
#Replace missing values
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['cast'].replace(np.nan, 'No Data',inplace  = True)
df['director'].replace(np.nan, 'No Data',inplace  = True)

#Drop values
df.dropna(inplace=True)
df.drop_duplicates(inplace= True)
df.isnull().sum()
df.info()

#Fixing dates
df["date_added"] = pd.to_datetime(df['date_added'])

df['month_added']=df['date_added'].dt.month
df['month_name_added']=df['date_added'].dt.month_name()
df['year_added'] = df['date_added'].dt.year

df.head(3)