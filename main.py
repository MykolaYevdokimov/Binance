
from binance import Client, ThreadedDepthCacheManager, ThreadedWebsocketManager
import pandas as pd
import mplfinance as mpf

from api import APIKEY, SECRETKEY

client = Client(APIKEY, SECRETKEY)

ticker = client.get_symbol_ticker(symbol= 'SOLUSDT')

ticker_symbol  = ticker['symbol']

ticket_price = ticker['price']

trades = client.get_historical_trades(symbol= ticker_symbol)

depth = client.get_order_book(symbol= ticker_symbol)

depth_df = pd.DataFrame(depth)

trades_df = pd.DataFrame(trades)


historical = client.get_historical_klines('SOLUSDT', Client.KLINE_INTERVAL_1DAY,'1 Jan 2024')  
'''
list of OHLCV values (Open time, Open, High, Low, Close, Volume, 
Close time, Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore)
'''


