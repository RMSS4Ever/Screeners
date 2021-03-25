import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download('SNDL', '2021-01-01', '2021-03-24')

print(data)

data.Close.plot()

plot.show()
