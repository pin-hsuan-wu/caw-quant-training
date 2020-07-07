import requests
import pandas as pd
import json
from pandas.io.json import json_normalize
import datetime

class get_data():
    def __init__(self, limit_in, toTs_in, nm):
        self.path = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit='+str(limit_in)+'&aggregate=1&toTs='+str(toTs_in)+'&e=binance'
        self.r = requests.get(self.path)
        self.outfilename = str(nm)+'.txt'
        self.infilename = str(nm)+'json'

        with open(self.outfilename, 'w') as fd:
            fd.write(self.r.text)

        with open(self.outfilename) as f:
            self.infilename = json.load(f)

test1 = get_data(10, 1585699200, 'try1')
test2 = get_data(10, 1578495600, 'try2')
print(test1.infilename)

class get_data_toplist():
    def __init__(self, limit_in, toTs_in, nm):
        self.path = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&limit='+str(limit_in)+'&aggregate=1&toTs='+str(toTs_in)+'&e=binance'
        self.r = requests.get(self.path)
        self.outfilename = str(nm)+'.txt'
        self.infilename = str(nm)+'json'

        with open(self.outfilename, 'w') as fd:
            fd.write(self.r.text)

        with open(self.outfilename) as f:
            self.infilename = json.load(f)