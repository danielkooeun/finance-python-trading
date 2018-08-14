import pandas as pd
import pandas_datareader as pdr
import quandl
import datetime

aapl = quandl.get('WIKI/AAPL', start_date='2006-10-01', end_date='2018-01-01')
aapl.to_csv('data/aapl_ohlc.csv')
df = pd.read_csv('data/aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)
