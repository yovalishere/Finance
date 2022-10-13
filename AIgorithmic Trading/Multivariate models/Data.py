import pandas as pd
import numpy as np
import datetime as dt
import bs4 as bs
import requests
import yfinance as yf
import os

def scraping_tickers():
    '''
    Scraping S&P 100 tickers symbols from Wikipedia
    '''
    from lib2to3.pytree import convert

    req=requests.get("https://en.wikipedia.org/wiki/S%26P_100")
    cvt=bs.BeautifulSoup(req.text,'lxml')
    tbl=cvt.find('table',{'class':"wikitable sortable"})

    tickers=[]
    for rows in tbl.find_all('tr')[1:]:
        ticker=rows.find_all('td')[0].text.strip()
        tickers.append(ticker)

    return tickers

def three_months_hist(tickers:list):
    ''' 
    Extract the 3 months of data of the tickers extracted (Real Time)
    '''
    
    all_data=pd.DataFrame()
    each_data=pd.DataFrame()
    no_data=[]

    for i in tickers:
        try:
            print(i)
            each_data=yf.download(i,period='3mo', interval='1d')
            each_data['symbol']=i
            all_data=all_data.append(each_data)
        except:
            no_data.append(i)
    
    return all_data

if __name__ == "__main__":
    print("start...")
    
    tickers=scraping_tickers()
    df=three_months_hist(tickers) 

    file_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(file_dir, '../Multivariate models/all_data.csv')
    df.to_csv(csv_path, index = False)

    print("end...")