import tushare as ts

df = ts.get_hist_data('600848')
df.plot()
