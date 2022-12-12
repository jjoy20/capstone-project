#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Exploratory Data Analysis Lab**
# 

# Estimated time needed: **30** minutes
# 

# In this module you get to work with the cleaned dataset from the previous module.
# 
# In this assignment you will perform the task of exploratory data analysis.
# You will find out the distribution of data, presence of outliers and also determine the correlation between different columns in the dataset.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# *   Identify the distribution of data in the dataset.
# 
# *   Identify outliers in the dataset.
# 
# *   Remove outliers from the dataset.
# 
# *   Identify correlation between features in the dataset.
# 

# ***
# 

# ## Hands on Lab
# 

# Import the pandas module.
# 

# In[1]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[2]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")


# ## Distribution
# 

# ### Determine how the data is distributed
# 

# The column `ConvertedComp` contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
# 
# This assumes 12 working months and 50 working weeks.
# 

# Plot the distribution curve for the column `ConvertedComp`.
# 

# In[3]:


# your code goes here
df['ConvertedComp'].plot(kind='kde')


# Plot the histogram for the column `ConvertedComp`.
# 

# In[4]:


# your code goes here
df['ConvertedComp'].plot(kind='hist',)


# What is the median of the column `ConvertedComp`?
# 

# In[5]:


# your code goes here
df['ConvertedComp'].median()


# How many responders identified themselves only as a **Man**?
# 

# In[6]:


# your code goes here

df['Gender'].value_counts()


# Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?
# 

# In[7]:


# your code goes here

df.groupby('Gender').median('ConvertedComp')


# Give the five number summary for the column `Age`?
# 

# **Double click here for hint**.
# 
# <!--
# min,q1,median,q3,max of a column are its five number summary.
# -->
# 

# In[8]:


## your code goes here
from numpy import percentile
minimum=df['Age'].min()
maximum=df['Age'].max()
median=df['Age'].median()
q = percentile(df['Age'], [25, 50, 75])
print("min=",minimum,"\nmax=",maximum,"\nmedian=",median,"\nq1=",q[0],"\nq3=",q[1])


# In[9]:


#easy and simple  method
df['Age'].describe()


# Plot a histogram of the column `Age`.
# 

# In[10]:


# your code goes here
df['Age'].plot(kind='hist',)


# ## Outliers
# 

# ### Finding outliers
# 

# Find out if outliers exist in the column `ConvertedComp` using a box plot?
# 

# In[31]:


# your code goes here
# your code goes here
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


# your code goes here

fig = px.box(df, y="ConvertedComp")

fig.show()


# Find out the Inter Quartile Range for the column `ConvertedComp`.
# 

# In[26]:


# df.dropna()
# df['ConvertedComp']


major=df['ConvertedComp'].value_counts().idxmax()
major
df['ConvertedComp'].fillna(major,inplace=True)
data_df = np.array(df['ConvertedComp'])
q1,q2, q3 = np.percentile(data_df, [25,50 ,75])
iqr = q3 - q1

#display interquartile range 
iqr
# df[['ConvertedComp']].isnull()
# df.dropna()


# Find out the upper and lower bounds.
# 

# In[22]:


# your code goes here
lower_bound = df['ConvertedComp'].min()
upper_bound = df['ConvertedComp'].max()


print("Lower Bound : ",lower_bound,"\nUpper Bound : ",upper_bound)


# Identify how many outliers are there in the `ConvertedComp` column.
# 

# In[28]:


# your code goes here
print('Outliers below:',df['ConvertedComp'].lt(q1 - 1.5*iqr).sum())
print('Outliers above:',df['ConvertedComp'].gt(q3 + 1.5*iqr).sum())
print('Outliers below:',df['ConvertedComp'].lt(q1 - 1.5*iqr).sum())
print('Median with outliers:',df['ConvertedComp'].median())
print('Median with outliers removed:',df[df['ConvertedComp'].le(q3 + 1.5*iqr)]['ConvertedComp'].median())
print('Mean with outliers removed:',df[df['ConvertedComp'].le(q3 + 1.5*iqr)]['ConvertedComp'].mean())


# Create a new dataframe by removing the outliers from the `ConvertedComp` column.
# 

# In[36]:


# your code goes here

# your code goes here
print(df.shape)
print(df['ConvertedComp'].gt(q3 + 1.5*iqr).shape)
df1 = df[df['ConvertedComp'].le(q3 + 1.5*iqr)]
print('total number in new dataset:',df1.shape[0])
df2=df[df['ConvertedComp'].gt(q3 + 1.5*iqr)]
print('total number of outliers removed:',df2.shape[0])


# ## Correlation
# 

# ### Finding correlation
# 

# Find the correlation between `Age` and all other numerical columns.
# 

# In[37]:


# your code goes here
df.corr()['Age']


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

# Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
