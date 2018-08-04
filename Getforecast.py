import tushare as ts
from sqlalchemy import create_engine
import csv
import pandas as pd
from  datetime import *
import time

engine = create_engine("postgresql://postgres:linxing@localhost/stock")

###业绩预告
df=ts.forecast_data(2017,3)
df.to_sql('forecast', engine, if_exists='append')