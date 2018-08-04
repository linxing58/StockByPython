import tushare as ts
from sqlalchemy import create_engine
import csv
import pandas as pd
from  datetime import *
import time

engine = create_engine("postgresql://postgres:linxing@localhost/stock")

# # #业绩报告
df=ts.get_report_data(2017,2)
df.to_sql('report', engine, if_exists='append')
