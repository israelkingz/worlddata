
import numpy as np
import pandas as pd

def ols_reg(filename):
    global df
    df = pd.read_csv(f"{filename}.csv")     #assumption: the directory of both files is same  
    print(df.head())

ols_reg('worlddata')

"""The dataset extracted from the world data shows 15 unique countries over the period of 10 years with GDP and social rating impact of the countries. """

df.head()

df.columns

df['Country'] =df['Country '].str.strip()

df.describe()

df['Country'].nunique()

df['Country'].unique()

df['Year'].nunique()

df['Year'].unique()

df.columns

df['GDP'].value_counts()

df['ratingimpact'].value_counts()

df.corr()

"""There are high correlation of years recorded over the impact ratings in the dataset. This shows that the occurence in the countires over the years has a huge effort on the social impact ratings in the countries. """

import matplotlib.pyplot as plt 
import seaborn as sns

plt.figure(figsize=(8,5))
sns.boxplot('GDP',data=df)

plt.figure(figsize=(8,5))
sns.boxplot('Year',data=df)

df['GDP'].mean()

df.describe()['GDP']

df.describe()['ratingimpact']

df.describe()['Year']

plt.figure(figsize=(8,5))
sns.countplot('ratingimpact',data=df,palette='ocean')

plt.figure(figsize=(10,8))
sns.barplot(y='Country',x='GDP',data=df,palette='flag')

def plotting_features(data):
    
    cols = [ col for col in data.columns]
 
    nrows= int(np.ceil(len(cols)/2))
    fig, ax = plt.subplots(
                        nrows=nrows, 
                        ncols=2, 
                        figsize=(12,8),   
                        constrained_layout=True)
    ax = ax.ravel()
 
    for i in range(len(cols)):
        if (data[cols[i]].dtypes == 'object') |(len(data[cols[i]].unique().tolist()) < 10): 
            
            sns.countplot(y = data[cols[i]], ax=ax[i])
            ax[i].set_title(f'{cols[i]} count')
 
        else:
            sns.histplot(x = data[cols[i]], ax=ax[i])
            ax[i].set_title(f'{cols[i]} distribution');

plotting_features(df)

