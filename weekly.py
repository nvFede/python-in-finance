import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

pd.set_option('display.width', 1200)
pd.set_option('display.max_columns', 50)

data = pd.read_csv('SPY.csv', parse_dates=True, index_col=0)

open = data.Open.resample('W-MON').last()
close = data.Close.resample('W-FRI').last().shift(-4, freq='D')
adjClose = data['Adj Close'].resample('W-FRI').last().shift(-4, freq='D')
low = data.Low.resample('W-MON').min()
high = data.High.resample('W-MON').max()
volume = data.Volume.resample('W-MON').sum()

weekly_data = pd.concat([open, high, low, close, adjClose, volume], axis=1)
