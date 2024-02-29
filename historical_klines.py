import pandas as pd
from client import client

historical = client.get_historical_klines('SOLUSDT', client.KLINE_INTERVAL_1DAY,'1 Jan 2022', '1 Jan 2023')
historical += client.get_historical_klines('SOLUSDT', client.KLINE_INTERVAL_1DAY,'2 Jan 2023', '1 Jan 2024')
historical += client.get_historical_klines('SOLUSDT', client.KLINE_INTERVAL_1DAY,'2 Jan 2024')

historical_df =pd.DataFrame(historical,
                            columns = ['Open time','Open','High', 'Low', 'Close', 'Volume', 
'Close time', 'Quote asset volume',' Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']
)

historical_df = historical_df.set_index('Open time')

historical_df.index = pd.to_datetime(historical_df.index, unit='ms', utc= True)

historical_df['Open'] = round(historical_df['Open'].astype(float),3)
historical_df['High'] = historical_df['High'].astype(float)
historical_df['Low'] = historical_df['Low'].astype(float)
historical_df['Close'] = historical_df['Close'].astype(float)
historical_df['Volume'] = historical_df['Volume'].astype(float)

