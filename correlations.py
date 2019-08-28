from MetaTrader5 import *
from datetime import date
import pandas as pd 
import matplotlib.pyplot as plt 

# Initializing MT5 connection 
MT5Initialize()
MT5WaitForTerminal()

print(MT5TerminalInfo())
print(MT5Version())

# Create currency watchlist for which correlation matrix is to be plotted
sym = ['WDO$', 'WIN$']

# Copying data to dataframe
d = pd.DataFrame()
for i in sym:
    rates = MT5CopyRatesFromPos(i, MT5_TIMEFRAME_M5, 0, 90)
    d[i] = [y.close for y in rates]
    
# Deinitializing MT5 connection
MT5Shutdown()

# Compute Percentage Change
rets = d.pct_change()

# Compute Correlation
corr = rets.corr()

# Plot correlation matrix
plt.figure(figsize=(10, 10))
plt.imshow(corr, cmap='RdYlGn', interpolation='none', aspect='auto')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr)), corr.columns);
plt.suptitle('Correlations Heat Map', fontsize=15, fontweight='bold')
plt.show()