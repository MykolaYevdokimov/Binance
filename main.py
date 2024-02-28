
from binance import Client, ThreadedDepthCacheManager, ThreadedWebsocketManager
import pandas as pd
from api import APIKEY, SECRETKEY

client = Client(APIKEY, SECRETKEY)

ticker = client.get_symbol_ticker(symbol= 'SOLUSDT')

ticker_symbol  = ticker['symbol']

ticket_price = ticker['price']

trades = client.get_historical_trades(symbol= ticker_symbol)

ticker_df = pd.DataFrame(trades)

depth = client.get_order_book(symbol= 'SOLUSDT')

historical = client.get_historical_klines('SOLUSDT', Client.KLINE_INTERVAL_1DAY,'1 Jan 2024')  #OHLCV (Open, High, Low, Close, Volume)



