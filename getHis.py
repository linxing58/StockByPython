import tushare as ts
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:linxing@132.232.16.101:5432/stock')
#一次性获取全部日k线数据
# ts.get_hist_data('600848')
#设定历史数据的时间
df = ts.get_stock_basics()
for indexs in df.index:
    hisdf=ts.get_hist_data(indexs,start='2017-01-01',end='2018-07-30')
    hisdf['code']=indexs
    hisdf.to_sql('hist_data', engine,if_exists='replace')

# ts.get_h_data('002337') #前复权
# ts.get_h_data('002337', autype='hfq') #后复权
# ts.get_h_data('002337', autype=None) #不复权
# ts.get_h_data('002337', start='2015-01-01', end='2015-03-16') #两个日期之间的前复权数据
#
# ts.get_h_data('399106', index=True) #深圳综合指数
#
# #实时行情
# ts.get_today_all()
#
# #历史分笔
# df = ts.get_tick_data('600848',date='2014-01-09')
# df.head(10)
#
# #实时分笔
# df = ts.get_realtime_quotes('000581') #Single stock symbol
# df[['code','name','price','bid','ask','volume','amount','time']]
#
# #当日历史分笔
# df = ts.get_today_ticks('601333')
# df.head(10)

# #大盘指数行情列表
# df = ts.get_index()
#
# #大单交易数据
# df = ts.get_sina_dd('600848', date='2015-12-24') #默认400手