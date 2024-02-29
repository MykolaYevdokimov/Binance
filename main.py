import pandas as pd
import mplfinance as mpf


from api import APIKEY, SECRETKEY
from client import client
from historical_klines import historical_df

'''ticker = client.get_symbol_ticker(symbol= 'SOLUSDT')

ticker_symbol  = ticker['symbol']

trades = client.get_historical_trades(symbol= ticker_symbol)

depth = client.get_order_book(symbol= ticker_symbol)

depth_df = pd.DataFrame(depth)

trades_df = pd.DataFrame(trades)

trades_df = trades_df.set_index('time')

trades_df.index = pd.to_datetime(trades_df.index, unit='ms', utc= True).strftime('%d %b %Y, %I:%M%p')'''

ohlcv = pd.DataFrame(historical_df,
                    columns = ['Open','High', 'Low', 'Close','Volume',]
)

'''
list of OHLCV values (Open time, Open, High, Low, Close, Volume, 
Close time, Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Ignore)
'''


kwargs = dict(type='candle',mav=(2),volume=True,figratio=(11,8), main_panel=1,volume_panel=0)

max_point = ohlcv[ohlcv['High'] == ohlcv['High'].max()]
min_point = ohlcv[ohlcv['Low'] == ohlcv['Low'].min()]

apds = []

mpf.plot(ohlcv, addplot = apds,**kwargs,style = 'charles')    


