from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://postgres:linxing@localhost/stock",
                       client_encoding='utf8')
result = engine.execute(
    'SELECT  date,count(*) from hist_data where price_change<0 and date>\'2017-01-01\' GROUP BY  date ORDER BY  date asc')
data = result.fetchall()
result.close()
df = pd.DataFrame(data)
df.plot()
