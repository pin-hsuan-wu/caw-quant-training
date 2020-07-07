from binance.client import Client
import pandas as pd
import datetime


client = Client('wtghA8np3ya8wxPql2z76afFiEjiMhMbYyxFRd7xEf8j5uO2qRg3AAKs6Cvk9POQ','JCdvfyvef1dy9j3TfHJkeQJuDmxgZ0Wfc92O6GaTiyBh5hMfDlYDVndjpT2ryEZK')

order = client.create_test_order(
    symbol='BTCUSDT',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=100)

