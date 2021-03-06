import pandas as pd
# bypass pdr error
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader as pdr
import datetime
import quandl
quandl.ApiConfig.api_key = '-nT3YEYhZVvDaJ5Bx9pE'

aapl = quandl.get('WIKI/AAPL', start_date='2006-10-01', end_date='2018-01-01')
aapl.to_csv('data/aapl_ohlc.csv')

# df will contain dataframe for AAPL time series data
aapl = pd.read_csv('data/aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)

def get(tickers, startdate, enddate):
  def data(ticker):
    return (quandl.get('WIKI/' + ticker, start_date=startdate, end_date=enddate))
  datas = map (data, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']
all_data = get(tickers, '2006-10-01', '2018-01-01')
all_data.to_csv('data/faang_stock.csv')