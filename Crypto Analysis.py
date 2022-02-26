#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')
dfb = pd.read_csv('btc-market-price.csv',header= None,names=['TimeStamp','Price'],index_col=0, parse_dates=True )
dfe= pd.read_csv('eth-price.csv', index_col=0, parse_dates=True)
prices= pd.DataFrame(index=dfb.index)
prices['Bitcoin']=dfb["Price"]
prices['Ethereaum']=dfe['Value']
prices.plot(figsize=(16,9))
null= prices.isnull()
prices.fillna(method='bfill', inplace=True)
prices.plot(figsize=(15,10))
prices.plot(kind='hist', y='Ethereaum', bins=100)
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(prices['Ethereaum'], ax=ax)
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(prices['Bitcoin'], rug=True, ax=ax)
fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(prices['Bitcoin'], ax=ax, hist_kws=dict(cumulative=True), kde_kws=dict(cumulative=True))
sns.jointplot(x="Bitcoin", y="Ethereaum", data=prices, size=5)



