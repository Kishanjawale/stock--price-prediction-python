import yfinance as yf
import pandas as pd 

data= yf.download("RELIANCE.NS")
data.to_csv("Reliance.csv")