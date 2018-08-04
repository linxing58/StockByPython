import tushare as ts
from sqlalchemy import create_engine
import csv
import pandas as pd
from datetime import *
import time

engine = create_engine("postgresql://postgres:linxing@localhost/stock")


# # #获取股票基本信息
df=ts.get_stock_basics()
df.to_csv('stock_basics.csv')
df.to_sql('stock_basics', engine, if_exists='append')