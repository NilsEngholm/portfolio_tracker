import yaml
import yfinance as yf
import pandas as pd
import requests

with open('template.yaml') as stonks:
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

tickerList = getSymbols(portfolio)
print(tickerList)