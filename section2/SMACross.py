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

class SMACross(bt.Strategy):
    
    params = (
        ('pfast', 5),
        ('pslow', 15),
    )

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.SMAfast = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.pfast)
        self.SMAslow = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.pslow)
        self.SMACross = bt.indicators.CrossOver(self.SMAfast, self.SMAslow)


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

            if self.SMACross[0] > 0:
                # BUY
                self.log('BUY CREATE, %.2f' % self.dataclose[0])
                self.order = self.buy()

        else:
            if self.SMACross[0] < 0:
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
    cerebro.addstrategy(SMACross)

    cerebro.addsizer(bt.sizers.PercentSizer, percents=99)
    cerebro.broker.set_cash(10000)
    cerebro.broker.setcommission(commission=0.001)

    cerebro.addwriter(
	bt.WriterFile, 
	out=os.path.join(logdir, 'BTC_USDT_SMACross_5_15_2020-01-01_2020-04-01.csv'),
	csv=True)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()
    
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    print(cerebro.strats[0][0][0])

    plt.rcParams['figure.figsize'] = [13.8, 10]
    fig = cerebro.plot(style='candlestick', barup='green', bardown='red')
    fig[0][0].savefig(
        os.path.join(reportdir, 'BTC_USDT_SMACross_5_15_2020-01-01_2020-04-01.png'),
        dpi=480)