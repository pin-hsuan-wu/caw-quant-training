from binance.client import Client
import pandas as pd
import datetime


with open("./binance_api.txt") as f:
    file = f.read()
key = file.split(',')[0]
secret = file.split(',')[1]

client = Client(api_key= key,api_secret= secret)

#Klines
klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020", "1 Apr, 2020")
kline_df = pd.DataFrame(klines, columns=['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
kline_df["Date"] = pd.to_datetime(kline_df['Open_time'], unit = 'ms')
kline_df = kline_df.drop(['Open_time','Close_time','Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'], axis=1)
kline_df.to_csv('BTC_USDT_kline.csv', index=False)

