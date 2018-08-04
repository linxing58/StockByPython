import tushare as ts
from sqlalchemy import create_engine
import csv
import pandas as pd
from  datetime import *
import time

engine = create_engine("postgresql://postgres:linxing@localhost/stock")
# 获取历史行情
with open("stock_basics.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stockcode = row['code']
        df = ts.get_k_data(stockcode,ktype='D',start='2016-01-01')
        df["code"] = pd.Series(stockcode, index=df.index)
        #日数据
        df.to_sql('k_day_data', engine, if_exists='append')
        df = ts.get_k_data(stockcode, ktype='W',start='2016-01-01')
        df["code"] = pd.Series(stockcode, index=df.index)
        #周数据
        df.to_sql('k_week_data', engine, if_exists='append')
        df = ts.get_k_data(stockcode, ktype='M',start='2016-01-01')
        df["code"] = pd.Series(stockcode, index=df.index)
        # 月数据
        df.to_sql('k_month_data', engine, if_exists='append')

        df = ts.get_hist_data(stockcode,start='2016-01-01')
        df["code"] = pd.Series(stockcode, index=df.index)
        #历史数据
        df.to_sql('hist_data', engine, if_exists='append')
# 获取今日行情
# df=ts.get_today_all()
# df.to_sql('today_all', engine, if_exists='append')
# 获取昨天行日
# today=date.today()
# yearstoday=today+timedelta(days=-1)
# today=today.strftime( '%Y-%m-%d' )
# yearstoday=yearstoday.strftime( '%Y-%m-%d' )
# with open ("stock_basics.csv") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         stockcode=row['code']
#         # df=ts.get_k_data(stockcode)
#         df = ts.get_hist_data(stockcode,start=yearstoday,end=yearstoday)
#         df["code"]=pd.Series(stockcode,index=df.index)
#         # 存入数据库
#         df.to_sql('yeasterday_all', engine, if_exists='append')
# # #获取股票基本信息
# df=ts.get_stock_basics()
# df.to_csv('stock_basics.csv')
# df.to_sql('stock_basics', engine, if_exists='append')
# # #业绩报告
# df=ts.get_report_data(2016,4)
# df.to_sql('report', engine, if_exists='append')
