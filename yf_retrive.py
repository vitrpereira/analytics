import yfinance as yf
import pandas as pd 

class YFinance:
    
    def __init__(self):
        ...

    def yf_to_pd(self, base_ticker):
        self.ticker = yf.Ticker(base_ticker)

        self.dataframe = pd.DataFrame.from_dict(self.ticker.info).rename(columns=str.lower)

        return self.dataframe
    
    def none():
        ...

instance = YFinance()

instance.yf_to_pd("NU")