import pandas as pd
# bypass pdr error
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader as pdr
import quandl
import datetime

# aapl = quandl.get('WIKI/AAPL', start_date='2006-10-01', end_date='2018-01-01')
# aapl.to_csv('data/aapl_ohlc.csv')

# df will contain dataframe for AAPL time series data
aapl = pd.read_csv('data/aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)

# indices contain the date values, columns show the data for each date
aapl_index = aapl.index
aapl_columns = aapl.columns

# returns Series
# print(aapl_columns[-10:])
# print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())
# print(aapl.loc['2007'].head())
# print(aapl.iloc[[22, 43], [0, 3]])

# Samples 20 rows (random)
sample = aapl.sample(20)
print(sample)

# Change sample to months
monthy_aapl = aapl.resample('M').mean()
print(monthy_aapl)