import pandas as pd 
import yfinance as yf

Equity_Details = pd.read_csv('EQUITY_L.csv')


for name in Equity_Details.SYMBOL:
    try:
        Data = yf.download(f'{name}.NS')
        Data.to_csv(f'./Data/{name}.csv')
    except Exception as e:
        print(f'{name} ==>> {e}')