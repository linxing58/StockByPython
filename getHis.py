import tushare as ts

#基础信息
dataframe=ts.get_stock_basics()
print(dataframe)
#业绩报表
ts.get_report_data(2018,2)
#盈利能力
ts.get_profit_data(2018,2)
#营运能力
ts.get_operation_data(2018,3)
#成长能力
ts.get_growth_data(2018,3)
#偿债能力
ts.get_debtpaying_data(2018,3)
#现金流量
ts.get_cashflow_data(2018,3)

#一次性获取全部日k线数据
ts.get_hist_data('600848')
#设定历史数据的时间
ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')

ts.get_h_data('002337') #前复权
ts.get_h_data('002337', autype='hfq') #后复权
ts.get_h_data('002337', autype=None) #不复权
ts.get_h_data('002337', start='2015-01-01', end='2015-03-16') #两个日期之间的前复权数据

ts.get_h_data('399106', index=True) #深圳综合指数

#实时行情
ts.get_today_all()

#历史分笔
df = ts.get_tick_data('600848',date='2014-01-09')
df.head(10)

#实时分笔
df = ts.get_realtime_quotes('000581') #Single stock symbol
df[['code','name','price','bid','ask','volume','amount','time']]

#当日历史分笔
df = ts.get_today_ticks('601333')
df.head(10)

#大盘指数行情列表
df = ts.get_index()

#大单交易数据
df = ts.get_sina_dd('600848', date='2015-12-24') #默认400手