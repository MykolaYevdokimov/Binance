import pandas as pd
from client import client
from sklearn.preprocessing import StandardScaler, MinMaxScaler



def get_historical_data(symbol,start_date, end_date = None, interval = '1d'):
    data = client.get_historical_klines(symbol, interval, start_date, end_date)
    df = pd.DataFrame(data, columns=['Open time', 'Open', 'High', 'Low', 'Close',
                                      'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 
                                      'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms', utc=True)
    df.set_index('Open time', inplace=True)
    df = df.astype({'Open': float, 'High': float, 'Low': float, 'Close': float, 'Volume': float})
    return df

def to_ohlc_type(df, value = False):
    if value:
        ohlc = pd.DataFrame(df,
                    columns = ['Open','High', 'Low', 'Close','Volume',]
        )
        return ohlc
 
    ohlc = pd.DataFrame(df,
                    columns = ['Open','High', 'Low', 'Close','Volume',]
    )
    return ohlc

def normalize_data_standard(df):#Стандартизация 
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(df[['Open', 'High', 'Low', 'Close', 'Volume']])
    normalized_df = pd.DataFrame(normalized_data, columns=['Open', 'High', 'Low', 'Close', 'Volume'], index=df.index)
    return normalized_df

def normalize_data_minMax(df): #Масштабирование 
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(df[['Open', 'High', 'Low', 'Close', 'Volume']])
    normalized_df = pd.DataFrame(normalized_data, columns=['Open', 'High', 'Low', 'Close', 'Volume'], index=df.index)
    return normalized_df
