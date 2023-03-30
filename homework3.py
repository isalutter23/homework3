#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:17:48 2023

@author: isabelllutter
"""

#homework3
import pandas as pd

######################################################
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import datetime as dt
import pandas_datareader.data as web 
import os
import yfinance as yfin

yfin.pdr_override()
plt.rc('figure', figsize=(10, 6)) 
pd.options.display.max_rows = 20 
np.set_printoptions(precision=4, suppress=True)

verbund = web.get_data_yahoo('VER.VI', start='2006-01-01', end='2023-03-28') 
erste_group_bank = web.get_data_yahoo('EBS.VI', start='2006-01-01', end='2023-03-28') 
omv = web.get_data_yahoo('OMV.VI', start='2006-01-01', end='2023-03-28') 
raiffeisen = web.get_data_yahoo('RBI.VI', start='2006-01-01', end='2023-03-28') 
immofinanz = web.get_data_yahoo('IIA.VI', start='2006-01-01', end='2023-03-28') 

stocks_dict = {'verbund': verbund, 'erste_group_bank': erste_group_bank,
                   'omv': omv, 'raiffeisen': raiffeisen, 'immofinanz': immofinanz}


stock_names = ['verbund', 'erste_group_bank', 'omv', 'raiffeisen', 'immofinanz']

print(verbund.count())
print(erste_group_bank.count())
print(omv.count())
print(raiffeisen.count())
print(immofinanz.count())


#ex2
rescaled_prices_df = pd.DataFrame()

verbund
verbund['Date'] = verbund.index

v_end_of_2019_price = [verbund['Date'] == '2019-12-31', 'Adj Close']
    rescaled_prices = stock_names['Adj Close'] / end_of_2019_price
    rescaled_prices_df[stock_names] = rescaled_prices


verbund.Date == '2006-01-05'




# Plot the rescaled adjusted closing prices for all stocks from 2019 to 2022
rescaled_prices_df.plot()
plt.title('Rescaled Adjusted Closing Prices from 2019 to 2022')
plt.xlabel('Date')
plt.ylabel('Rescaled Adjusted Closing Price')
plt.show()