from binance.client import Client
import pandas as pd
import datetime

with open("./binance_api.txt") as f:
    file = f.read()
key = file.split(',')[0]
secret = file.split(',')[1]

client = Client(api_key= key,api_secret= secret)

#Klines
klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020")
kline_df = pd.DataFrame(klines, columns=['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'])
kline_df["Open time"] = pd.to_datetime(kline_df['Open_time'], unit = 'ms')
kline_df["Close time"] = pd.to_datetime(kline_df['Close_time'], unit = 'ms')
kline_df["Close time"] = kline_df["Close time"].dt.round("H")
kline_df = kline_df.drop(["Open_time","Close_time"], axis=1)
kline_df.to_csv('kline.csv', index=False)

#Trades
recent_trades = client.get_recent_trades(symbol='BTCUSDT')
rt_df = pd.DataFrame(recent_trades)
rt_df['date time'] = pd.to_datetime(rt_df['time'], unit = 'ms')
rt_df['date time'] = rt_df['date time'].dt.round("S")
rt_df = rt_df.drop("time", axis=1)
rt_df.to_csv('recent_trades.csv', index=False)

#Depth
depth = client.get_order_book(symbol='BTCUSDT')
depth_df = pd.DataFrame(depth)
depth_df['bids_price'] = depth_df.bids.apply(lambda x: x[0])
depth_df['bids_qty'] = depth_df.bids.apply(lambda x: x[1])
depth_df['asks_price'] = depth_df.asks.apply(lambda x: x[0])
depth_df['asks_qty'] = depth_df.asks.apply(lambda x: x[1])
depth_df = depth_df.drop(["bids","asks"], axis=1)
depth_df.to_csv('depth.csv', index=False)

#Optional
order = client.create_test_order(
    symbol='BTCUSDT',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)
