#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Yahoo! Finance market data downloader (+fix for Pandas Datareader)
# https://github.com/ranaroussi/yfinance



import yfinance as yf
import unittest
import urllib
import time as tm


# NOTE: Some stocks may be delisted as this data is on the older side, but it should still work for our purposes
testdata = open("nyse_data.txt","r")

symbols = testdata.read()

symbols = symbols.split("\n")




def test_class(symbol):
    data = yf.download(  # or pdr.get_data_yahoo(...
    # tickers list or string as well
    tickers = symbol,

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period = "ytd",

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval = "1d",

    start="2020-01-28", 


    end="2021-02-05",

    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    group_by = 'ticker',

    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust = True,

    # download pre/post regular market hours data
    # (optional, default is False)
    prepost = True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads = True,

    # proxy URL scheme use use when downloading?
    # (optional, default is None)
    proxy = None,

    actions = True,

    rounding = True
    )
    if len(data) == 0:
        print("Failed class test")
    else:
        print("Passed class test")


def test_download(symbols):
    data = yf.download(  # or pdr.get_data_yahoo(...
    # tickers list or string as well
    tickers = symbols,

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period = "ytd",

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval = "1d",

    start="2020-01-28", 


    end="2021-02-05",

    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    group_by = 'ticker',

    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust = True,

    # download pre/post regular market hours data
    # (optional, default is False)
    prepost = True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads = True,

    # proxy URL scheme use use when downloading?
    # (optional, default is None)
    proxy = None,

    actions = True,

    rounding = True
    )
    if None in data:
        print("Failed download test")
    else:
        print("Passed download test")

def test_download_hang(symbols):
    t0= tm.process_time()
    data = yf.download(  # or pdr.get_data_yahoo(...
    # tickers list or string as well
    tickers = symbols,

    # use "period" instead of start/end
    # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    # (optional, default is '1mo')
    period = "ytd",

    # fetch data by interval (including intraday if period < 60 days)
    # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    # (optional, default is '1d')
    interval = "1d",

    start="2020-01-28", 


    end="2021-02-05",

    # group by ticker (to access via data['SPY'])
    # (optional, default is 'column')
    group_by = 'ticker',

    # adjust all OHLC automatically
    # (optional, default is False)
    auto_adjust = True,

    # download pre/post regular market hours data
    # (optional, default is False)
    prepost = True,

    # use threads for mass downloading? (True/False/Integer)
    # (optional, default is True)
    threads = True,

    # proxy URL scheme use use when downloading?
    # (optional, default is None)
    proxy = None,

    actions = True,

    rounding = True
    )
    t1 = tm.process_time()
    # If download took longer than 10 minutes (it never should and thread will likely timeout if this happens anyway, which is why I'm checking if download took that long)
    if t1 - t0 > 6000:
        print("Failed hang test")
    else:
        print("Passed hang test")
    

test_class("BRK-A")
test_class("BRK.A")

# test_download(symbols)

# test_download_hang(symbols[1:1000])


