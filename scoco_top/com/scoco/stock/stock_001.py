import pandas.io.data

import pandas_datareader.data as web

start = datetime.datetime(2018,1,1)
end = datetime.date.today()
stock = web.DataReader("600797.SS", "yahoo", start, end)
print(stock.head(5))
print(stock.tail(5))