import pandas as pd
import matplotlib.pyplot as plt

#parse_dates = True ( analizamos los datos)
#index_col = 0 ( primera columna)
data = pd.read_csv('acciones.csv', parse_dates=True, index_col=0)

#linea roja y de grosor 2
data['AAPL'].plot(lw=2, c='r')
plt.show()
