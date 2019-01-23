import pandas as pd
import fix_yahoo_finance as yf
from datetime import datetime, timedelta

#definir el periodo temporal que deseamos descargar
#en este caso seria la fecha actual, menos 252 dias
start = datetime.today() - timedelta(days=252)
end = datetime.today()

#descargar de yahoo finance
data = yf.download(['AAPL', 'AMZN', 'FB'], start, end)['Adj Close']

data.to_csv('acciones.csv')

print(data.head(10))
