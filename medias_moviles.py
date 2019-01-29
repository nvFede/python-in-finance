import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns

sns.set()

#modificamos las opciones para ver mas columnas y mas filas del dataframe
pd.set_option('display.width', 1200)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 5000)


dir_path = os.path.dirname(os.path.realpath(__file__))
file = dir_path + '/SPY.csv'
data = pd.read_csv(file, parse_dates=True, index_col=0)
data.dropna(inplace=True)
short_avg = 18
long_avg = 40

signals = pd.DataFrame(index=data.index)
signals['signal'] = 0.0

signals['short_avg'] = data['Close'].rolling(short_avg).mean()
signals['long_avg'] = data['Close'].rolling(long_avg).mean()
#
signals['signal'][short_avg:] = np.where(signals['short_avg'][short_avg:] > signals['long_avg'][short_avg:], 1.0, 0.0)

signals['position'] = signals['signal'].diff()
signals.dropna(inplace=True)
print(signals)

ax1 = plt.subplot()
ax1.plot(data['Close'])
ax1.plot(signals['short_avg'])
ax1.plot(signals['long_avg'])

# dibujar señales de compra
ax1.plot(signals.loc[signals.position == 1.0].index, signals.short_avg[signals.position == 1.0],
    '^', markersize=15, c='g')
# dibujar señales de venta
ax1.plot(signals.loc[signals.position == -1.0].index, signals.short_avg[signals.position == -1.0], '*', markersize=15, c='r')
plt.show()
