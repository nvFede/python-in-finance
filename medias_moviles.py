import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('SPY.csv', parse_dates=True, index_col=0)

short_avg = 18
long_avg = 40

signals = pd.DataFrame(index=data.index)
signals['signal'] = 0.0

signals['short_avg'] = data['Close'].rolling(short_avg).mean()
signals['long_avg'] = data['Close'].rolling(long_avg).mean()

signals['signal'][short_avg:] = np.where(signals['short_avg'][short_avg:] > signals['long_avg'][long_avg], 1.0, 0.0)

signals['positions'] = signals['signal'].diff()
signals.dropna()
print(signals)
#
# data['Close'].plot()
# signals['short_avg'].plot()
# signals['long_avg'].plot()
# plt.show()
