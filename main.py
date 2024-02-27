
from binance import Client, ThreadedDepthCacheManager, ThreadedWebsocketManager
import pandas as pd
from api import APIKEY, SECRETKEY

client = Client(APIKEY, SECRETKEY)

tickers = client.get_all_tickers()

ticker_df = pd.DataFrame(tickers)

ticker_df.set_index('symbol', inplace=True)

depth = client.get_order_book(symbol= 'SOLUSDT') #glass

historical = client.get_historical_klines('SOLUSDT', Client.KLINE_INTERVAL_1DAY,'1 Jan 2024') 

print(historical)