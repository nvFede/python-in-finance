import pandas as pd


#parse_dates = True ( analizamos los datos)
#index_col = 0 ( primera columna)
data = pd.read_csv('acciones.csv', parse_dates=True, index_col=0)

#mostramos las 10 primeras filas del dataframe
print(data.head(10))
