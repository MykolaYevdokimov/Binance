import pandas as pd
from client import client
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def get_historical_data(symbol, interval, start_date, end_date = None):
    data = client.get_historical_klines(symbol, interval, start_date, end_date)
    df = pd.DataFrame(data, columns=['Open time', 'Open', 'High', 'Low', 'Close',
                                      'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 
                                      'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
    df['Open time'] = pd.to_datetime(df['Open time'], unit='ms', utc=True)
    df.set_index('Open time', inplace=True)
    df = df.astype({'Open': float, 'High': float, 'Low': float, 'Close': float, 'Volume': float})
    return df

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


# Пример использования:
'''
historical_df = get_historical_data('SOLUSDT', client.KLINE_INTERVAL_1DAY, '1 Jan 2022', '2 Jan 2024')
normalized_standard_df = normalize_data_standard(historical_df)
normalized_MinMax_df = normalize_data_MinMax(historical_df)
print(historical_df)'''