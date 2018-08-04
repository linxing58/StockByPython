import tushare as ts
from sqlalchemy import create_engine
import csv
import pandas as pd
from  datetime import *
import time

engine = create_engine("postgresql://postgres:linxing@localhost/stock")

# 获取今日行情
df=ts.get_today_all()
df.to_sql('today_all', engine, if_exists='append')
# 获取昨天行日
today=date.today()
yearstoday=today+timedelta(days=-1)
today=today.strftime( '%Y-%m-%d' )
yearstoday=yearstoday.strftime( '%Y-%m-%d' )
with open ("stock_basics.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stockcode=row['code']
        # df=ts.get_k_data(stockcode)
        df = ts.get_hist_data(stockcode,start=yearstoday,end=yearstoday)
        df["code"]=pd.Series(stockcode,index=df.index)
        # 存入数据库
        df.to_sql('yeasterday_all', engine, if_exists='append')
