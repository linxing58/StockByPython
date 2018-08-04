from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://postgres:linxing@localhost/stock",
                       client_encoding='utf8')
coderesult = engine.execute(
    'select code,name,industry,area from stock_basics')
basicdata = coderesult.fetchall()
coderesult.close()
basicdf = pd.DataFrame(basicdata)
stock_code = ""
for stock in range(0, basicdf.__len__()):
    stock_code = basicdf[0][stock]
    cstock_kdataresult = engine.execute(
        'SELECT  code,date,open,close,high,low  from k_day_data where code=\'' + stock_code + '\'  ORDER BY  date asc')
    stock_kdata = cstock_kdataresult.fetchall()
    cstock_kdataresult.close()
    stock_df = pd.DataFrame(stock_kdata)
    # stock_df.rename(columns={'0':'code','1':'date','2':'open','3':'close','4':'high','5':'low'},inplace=True)
    stock_df.columns = ['code', 'date', 'open', 'close', 'high', 'low']
    stock_df["ema12"] = pd.Series(0, index=stock_df.index, dtype='float64')
    stock_df["ema26"] = pd.Series(0, index=stock_df.index, dtype='float64')
    stock_df["dif"] = pd.Series(0, index=stock_df.index, dtype='float64')
    stock_df["dea"] = pd.Series(0, index=stock_df.index, dtype='float64')
    stock_df["macd"] = pd.Series(0, index=stock_df.index, dtype='float64')
    for k_index in range(0, stock_df.__len__() - 2):
        print(k_index)
        stock_df["ema12"][k_index + 1] = stock_df["ema12"][k_index] * (11 / 13) + stock_df["close"][k_index + 1] * (
            2 / 13)
        stock_df["ema26"][k_index + 1] = stock_df["ema26"][k_index] * (25 / 27) + stock_df["close"][k_index + 1] * (
            2 / 27)
        stock_df["dif"][k_index + 1] = stock_df["ema12"][k_index + 1] - stock_df["ema26"][k_index + 1]
        stock_df["dea"][k_index + 1] = stock_df["dif"][k_index + 1] - stock_df["dea"][k_index]
        stock_df["macd"][k_index + 1] = (stock_df["dif"][k_index + 1] - stock_df["dea"][k_index + 1]) * 2
    stock_df.to_sql('macd', engine, if_exists='append')
