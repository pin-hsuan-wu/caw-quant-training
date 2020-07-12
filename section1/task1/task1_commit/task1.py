import requests
import pandas as pd
import json
from pandas.io.json import json_normalize
import datetime

#r_2020_04_01 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1585699200&e=binance')

#with open('2020_04_01.txt', 'w') as fd: 
#    fd.write(r_2020_04_01.text)

#r_2020_01_08 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1578495600&e=binance')

#with open('2020_01_08.txt', 'w') as fd: 
#    fd.write(r_2020_01_08.text)

#r_2019_10_17 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1571292000&e=binance')

#with open('2019_10_17.txt', 'w') as fd: 
#    fd.write(r_2019_10_17.text)

#r_2019_07_25 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1564088400&e=binance')

#with open('2019_07_25.txt', 'w') as fd: 
#    fd.write(r_2019_07_25.text)

#r_2019_05_03 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1556884800&e=binance')

#with open('2019_05_03.txt', 'w') as fd: 
#    fd.write(r_2019_05_03.text)

#r_2019_02_09 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1549681200&e=binance')

#with open('2019_02_09.txt', 'w') as fd: 
#    fd.write(r_2019_02_09.text)

#r_2018_11_17 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1542477600&e=binance')

#with open('2018_11_17.txt', 'w') as fd: 
#    fd.write(r_2018_11_17.text)

#r_2018_08_26 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1535274000&e=binance')

#with open('2018_08_26.txt', 'w') as fd: 
#    fd.write(r_2018_08_26.text)

#r_2018_06_04 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1528070400&e=binance')

#with open('2018_06_04.txt', 'w') as fd: 
#    fd.write(r_2018_06_04.text)

#r_2018_03_12 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1520866800&e=binance')

#with open('2018_03_12.txt', 'w') as fd: 
#    fd.write(r_2018_03_12.text)

#r_2017_12_19 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1513663200&e=binance')

#with open('2017_12_19.txt', 'w') as fd: 
#    fd.write(r_2017_12_19.text)

#r_2017_09_26 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1506459600&e=binance')

#with open('2017_09_26.txt', 'w') as fd: 
#    fd.write(r_2017_09_26.text)

#r_2017_07_05 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=2000&aggregate=1&toTs=1499256000&e=binance')

#with open('2017_07_05.txt', 'w') as fd: 
#    fd.write(r_2017_07_05.text)

#r_2017_04_13 = requests.get('https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit=291&aggregate=1&toTs=1492052400&e=binance')

#with open('2017_04_13.txt', 'w') as fd: 
#    fd.write(r_2017_04_13.text)


#with open('2020_04_01.txt') as f1, open('2020_01_08.txt') as f2, open('2019_10_17.txt') as f3, open('2019_07_25.txt') as f4, open('2019_05_03.txt') as f5, open('2019_02_09.txt') as f6, open('2018_11_17.txt') as f7, open('2018_08_26.txt') as f8, open('2018_06_04.txt') as f9, open('2018_03_12.txt') as f10, open('2017_12_19.txt') as f11, open('2017_09_26.txt') as f12, open('2017_07_05.txt') as f13, open('2017_04_13.txt') as f14: 
#    json_2020_04_01 = json.load(f1)
#    json_2020_01_08 = json.load(f2)
#    json_2019_10_17 = json.load(f3)
#    json_2019_07_25 = json.load(f4)
#    json_2019_05_03 = json.load(f5)
#    json_2019_02_09 = json.load(f6)
#    json_2018_11_17 = json.load(f7)
#    json_2018_08_26 = json.load(f8)
#    json_2018_06_04 = json.load(f9)
#    json_2018_03_12 = json.load(f10)
#    json_2017_12_19 = json.load(f11)
#    json_2017_09_26 = json.load(f12)
#    json_2017_07_05 = json.load(f13)
#    json_2017_04_13 = json.load(f14) 

#json_list = [json_2020_04_01, json_2020_01_08, json_2019_10_17, json_2019_07_25, json_2019_05_03, json_2019_02_09, json_2018_11_17, json_2018_08_26, json_2018_06_04, json_2018_03_12, json_2017_12_19, json_2017_09_26, json_2017_07_05, json_2017_04_13]
#d = {}
#for i in range(0,14):
#    d[i] = json_normalize(json_list[i])

#d_df ={}
#for i in range(0,14):
#    d_df[i] = pd.DataFrame(d[i]["Data.Data"][0])

#frames = [d_df[13], d_df[12], d_df[11], d_df[10], d_df[9], d_df[8], d_df[7], d_df[6], d_df[5], d_df[4], d_df[3], d_df[2], d_df[1], d_df[0]]
#result = pd.concat(frames)

#result.to_csv('con_raw.csv')

#df = pd.read_csv("con_raw.csv")
#df["datetime"] = pd.to_datetime(df['time'], unit = 's')
#df = df.rename({"volumefrom":"volume","volumeto":"baseVolume"}, axis='columns')
#df = df[(['close', 'high', 'low', 'open', 'volume', 'baseVolume', 'datetime'])]
#df.volume = df.volume.round(3)
#df.to_csv('BTC_USDT_Hourly.csv', index=False)

#Optional

class  CryptoCompareAPI():
    def __init__(self):
        self.url = 'https://min-api.cryptocompare.com/data/'

    def get_hr_data(self, fsym, tsym, limit=168, agg=1, toTs=None, e='CCCAGG'):
        path = self.url + 'v2/histohour?fsym={}&tsym={}&limit={}&aggregate={}&toTs={}&e={}'.format(fsym, tsym, limit, agg, toTs, e)
        if limit > 2000:
            raise Exception('Max is 2000')
        else:
            r = requests.get(path)
            return r
    
    def get_top_mkt_data(self, limit, page, tsym):
        path = self.url + 'top/mktcapfull?limit={}&page={}&tsym={}'.format(limit, page, tsym)
        if limit > 100 or limit < 10:
            raise Exception('Min is 10 and Max is 100')
        else:
            r = requests.get(path)
            return r

api = CryptoCompareAPI()

test1 = api.get_hr_data('BTC', 'USDT', 2001, 1, 1585699200, 'binance')
print(test1.text)

test2 = api.get_top_mkt_data(5, 1, 'USD')
print(test2.text)
