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

historical = client.get_historical_klines('SOLUSDT', Client.KLINE_INTERVAL_1DAY,'1 Jan 2024')  

'''depth_df = pd.DataFrame(depth)

trades_df = pd.DataFrame(trades)


trades_df = trades_df.set_index('time')

trades_df.index = pd.to_datetime(trades_df.index, unit='ms', utc= True).strftime('%d %b %Y, %I:%M%p')'''

historical_df =pd.DataFrame(historical,
                            columns = ['Open time','Open','High', 'Low', 'Close', 'Volume', 
'Close time', 'Quote asset volume',' Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore']
)
 
historical_df = historical_df.set_index('Open time')

historical_df.index = pd.to_datetime(historical_df.index, unit='ms', utc= True)

ohlcv = pd.DataFrame(historical_df,
                    columns = ['Open','High', 'Low', 'Close','Volume',]
)


ohlcv['Open'] = ohlcv['Open'].astype(float)
ohlcv['High'] = ohlcv['High'].astype(float)
ohlcv['Low'] = ohlcv['Low'].astype(float)
ohlcv['Close'] = ohlcv['Close'].astype(float)
ohlcv['Volume'] = ohlcv['Volume'].astype(float)

print(ohlcv)

'''
list of OHLCV values (Open time, Open, High, Low, Close, Volume, 
Close time, Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore)
'''
mpf.plot(ohlcv)    


