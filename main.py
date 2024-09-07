import os
import requests
import yaml
import pandas as pd
from datetime import datetime, timedelta

#load config file
with open('secret.yaml') as stonks:
    try:
        cfg = yaml.safe_load(stonks)
        print('Config file loaded successfully')
    except yaml.YAMLError as exc:
        print(exc)

#load portfolio data from config file
portfolio = cfg['portfolio']

#list all ticker symbols in portfolio
def getSymbols(portfolio):
    symbols = []
    for holding in portfolio:
        symbols.append(holding)
    return symbols

# get stock data for each holding in portfolio
def getStockData(tickerList):
    #initialize list to store portfolio data
    portfolioData = []
    #iterate through each holding in portfolio
    for holding in tickerList:
        print(f"Getting stock data for {holding}")
        #define url to for API call
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={holding}&apikey={cfg["secretKey"]}'
        #send request to API | get response | convert to json | append to portfolioData list
        response = requests.get(url)
        data = response.json()
        portfolioData.append(data)
    #return portfolio data
    return portfolioData
        

tickerList = getSymbols(portfolio)

stockData = getStockData(tickerList)
print(stockData)