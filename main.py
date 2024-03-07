import pandas as pd
import mplfinance as mpf

from api import APIKEY, SECRETKEY
from client import client
from tokens import get_historical_data, to_ohlc_type, normalize_data_standard, normalize_data_minMax



tokens_pair_list = ['BTCUSDT', 'ETCUSDT', 'SOLUSDT']

ohlcv = to_ohlc_type((get_historical_data('ETCUSDT', '1 Jan 2022', '2 Jan 2024', '1d',)),value=True)

print(ohlcv)
print(ohlcv['Open'].max())