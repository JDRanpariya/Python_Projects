import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2001, 11, 20)
end = dt.datetime(2020, 11, 20)

# df = web.DataReader('TSLA', 'yahoo', start, end)

# df.to_csv('tsla.csv') // converts dataframe to csv

df = pd.read_csv('tsla.csv', parse_dates=True)
# print(df.head())
df.plot()
plt.show()
