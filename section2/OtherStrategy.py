import os
import datetime
import backtrader as bt
import pandas as pd
import matplotlib as plt

datadir = './section2/data/' # data path
logdir = './section2/log/' # log path
reportdir = './section2/report/' # report path
datafile = 'BTC_USDT_kline.csv' # data file
from_datetime = '2020-01-01 00:00:00' # start time 
to_datetime = '2020-04-01 00:00:00' # end time

class TestStrategy(bt.Strategy):
    
    params = (
        ('maperiod', 15),
        ('macd1', 12),
        ('macd2', 26),
        ('macdsig', 9),
    )

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.rsi = bt.indicators.RSI_EMA(
            self.datas[0], period=self.params.maperiod)
        self.macd = bt.indicators.MACD(self.datas[0],
                                   period_me1=self.params.macd1,
                                   period_me2=self.params.macd2,
                                   period_signal=self.params.macdsig) 
        self.mcross = bt.indicators.CrossOver(self.macd.macd, self.macd.signal)
        self.aup = bt.indicators.AroonUp(self.datas[0], period=self.params.maperiod)
        self.SMA = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.maperiod)


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.comm))

            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.comm))

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

    def next(self):
        self.log('Close, %.2f' % self.dataclose[0])
            
        if self.order:
            return
            
        if not self.position:

            if (self.rsi <= 30 or self.mcross[0] > 0.0) and self.aup >= 50:
                # BUY
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.order = self.buy()

        else:
            if self.dataclose[0] > self.SMA[0]:
                # SELL
                self.log('SELL CREATE, %.2f' % self.dataclose[0])
                self.order = self.sell()


if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    data = pd.read_csv(
        os.path.join(datadir, datafile), index_col='Date', parse_dates=True)
    data = data.loc[
        (data.index >= pd.to_datetime(from_datetime)) &
        (data.index <= pd.to_datetime(to_datetime))]
    datafeed = bt.feeds.PandasData(dataname=data)
    cerebro.adddata(datafeed)

    # Add a strategy
    cerebro.addstrategy(TestStrategy)

    cerebro.addsizer(bt.sizers.PercentSizer, percents=99)
    cerebro.broker.set_cash(10000)
    cerebro.broker.setcommission(commission=0.001)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()
    
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.plot()