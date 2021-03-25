import pandas as pd
import yfinance as yf
# import yahoo_fin.stock_info as si

print('Hello Brian. yFinance is loaded for you.')

data = yf.download('SNDL', '2021-03-022', '2021-03-23')

print(data)

