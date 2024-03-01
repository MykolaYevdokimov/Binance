import pandas as pd
import mplfinance as mpf

from api import APIKEY, SECRETKEY
from client import client
from historical_klines import get_historical_data, normalize_data_minMax, normalize_data_standard


historical_df = get_historical_data('SOLUSDT', client.KLINE_INTERVAL_1DAY, '1 Jan 2022', '2 Jan 2024')
normalize_data_minMax = normalize_data_minMax(historical_df)

ohlcv = pd.DataFrame(historical_df,
                    columns = ['Open','High', 'Low', 'Close','Volume',]
)

