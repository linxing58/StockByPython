from sqlalchemy import create_engine
import tushare as ts


engine = create_engine('postgresql+psycopg2://postgres:linxing@132.232.16.101:5432/stock')
#基础信息
df=ts.get_stock_basics()
df.to_sql('stock_basics',engine,if_exists='replace')
#业绩报表
df=ts.get_report_data(2018,2)
df.to_sql('report_data',engine,if_exists='replace')
#盈利能力
df=ts.get_profit_data(2018,2)
df.to_sql('profit_data',engine,if_exists='replace')
#营运能力
df=ts.get_operation_data(2018,2)
df.to_sql('operation_data',engine,if_exists='replace')
#成长能力
df=ts.get_growth_data(2018,2)
df.to_sql('growth_data',engine,if_exists='replace')
#偿债能力
df=ts.get_debtpaying_data(2018,2)
df.to_sql('debtpaying_data',engine,if_exists='replace')
#现金流量
df=ts.get_cashflow_data(2018,2)
df.to_sql('cashflow_data',engine,if_exists='replace')
