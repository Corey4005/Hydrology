# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:04:45 2021

@author: cwalker
"""
#import the needed packages. 
import dataretrieval.nwis as nwis
import matplotlib.pyplot as plt
import pandas as pd

#label the site
site = '02471001'

#get the record from nwis
df = nwis.get_record(sites=site, service='iv', start='2001-09-02', end='2021-09-09') 
df.index = pd.to_datetime(df.index, utc=True)

#set up the new dataframe for '00060'
discharge = df['00060']
index = discharge.groupby(discharge.index.year)

#calculate the stats
mean_annual_flow = index.mean()
mean_annual_peak_flow = index.max()

#plot the annual flow, peak flow and seven day annual
fig, ax = plt.subplots(figsize=(7,4))
mean_annual_flow.plot(ax=ax, label='Mean Annual Flow')
mean_annual_peak_flow.plot(ax=ax, label='Mean Annual Peak Flow')

#create the plot labels
ax.set_ylabel('Discharge - cubic feet per second')
ax.set_xlabel('Date')
ax.set_title('Discharge by Date - 20 years, USGS Station #02471001')
ax.legend(loc='best')



