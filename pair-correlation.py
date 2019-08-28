from MetaTrader5 import *
from datetime import date
import pandas as pd 
import matplotlib.pyplot as plt 

# Importing statmodels for cointegration test
import statsmodels
from statsmodels.tsa.stattools import coint

# Initializing MT5 connection 
MT5Initialize()
MT5WaitForTerminal()

print(MT5TerminalInfo())
print(MT5Version())

# Create currency watchlist for which correlation matrix is to be plotted
sym = ['PETR3', 'PETR4']

# Copying data to dataframe
d = pd.DataFrame()
for i in sym:
    rates = MT5CopyRatesFromPos(i, MT5_TIMEFRAME_D1, 0, 90)
    d[i] = [y.close for y in rates]

# Deinitializing MT5 connection
MT5Shutdown()

x = d[sym[0]]
y = d[sym[1]]
x = (x-min(x))/(max(x)-min(x))
y = (y-min(y))/(max(y)-min(y))

score = coint(x, y)
print('t-statistic: ', score[0], ' p-value: ', score[1])

# Plotting z-score transformation
diff_series = (x - y)
zscore = (diff_series - diff_series.mean()) / diff_series.std()

plt.plot(zscore)
plt.axhline(2.0, color='red', linestyle='--')
plt.axhline(-2.0, color='green', linestyle='--')

plt.show()