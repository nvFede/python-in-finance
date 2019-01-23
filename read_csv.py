import pandas as pd

#modificamos las opciones para ver mas columnas del dataframe
pd.set_option('display.width', 1200)
pd.set_option('display.max_columns', 50)

#parse_dates = True ( analizamos los datos)
#index_col = 0 ( primera columna)
data = pd.read_csv('acciones.csv', parse_dates=True, index_col=0)

#mostramos las 10 primeras filas del dataframe
print(data.head(10))
