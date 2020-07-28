import os
import datetime
import backtrader as bt
import pandas as pd
import numpy as np
import matplotlib as plt
import backtrader.analyzers as btanalyzers
import backtrader.feeds as btfeeds
import backtrader.strategies as btstrats
import scipy.stats as ss
import csv

datadir = './section2/data/' # data path
logdir = './section2/log/' # log path
reportdir = './section2/report/' # report path
datafile = 'BTC_USDT_1h.csv' # data file
from_datetime = '2020-01-01 00:00:00' # start time 
to_datetime = '2020-04-01 00:00:00' # end time

# Create a Stratey
class SMACross(bt.Strategy):
    params = (
        ('pfast', 15),
        ('pslow', 23),
        ('printlog', False),
    )

    def log(self, txt, dt=None, doprint=False):
        ''' Logging function fot this strategy'''
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None
        self.SMAfast = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.pfast)
        self.SMAslow = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.pslow)
        self.SMACross = bt.indicators.CrossOver(self.SMAfast, self.SMAslow)


    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        self.order = None

    def next(self):

        if self.order:
            return

        # Check if we are in the market
        if not self.position:

            if self.SMACross[0] > 0:
                self.order = self.buy()

        else:

            if self.SMACross[0] < 0:
                self.order = self.sell()



if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro(optreturn=False)

    strats = cerebro.optstrategy(
        SMACross,
        pfast=range(10, 16),
        pslow=range(20, 26))

    data = pd.read_csv(
        os.path.join(datadir, datafile), index_col='datetime', parse_dates=True)
    data = data.loc[
        (data.index >= pd.to_datetime(from_datetime)) &
        (data.index <= pd.to_datetime(to_datetime))]
    datafeed = bt.feeds.PandasData(dataname=data)
    cerebro.adddata(datafeed)

    cerebro.addsizer(bt.sizers.PercentSizer, percents=99)
    cerebro.broker.set_cash(10000)
    cerebro.broker.setcommission(commission=0.001)
    
    #Analyzer
    cerebro.addanalyzer(bt.analyzers.DrawDown)
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer)

    optimized_runs = cerebro.run()

    final_results_list = []
    rtlist = []
    maxdnlist = []
    wtlist = []
    awllist = []
    for run in optimized_runs:
        for strategy in run:
            rt = (strategy.broker.getvalue()/10000)-1
            dd = strategy.analyzers.drawdown.get_analysis()
            tt = strategy.analyzers.tradeanalyzer.get_analysis()
            wt = tt.won.total/tt.total.closed
            aw = tt.won.pnl.average
            al = tt.lost.pnl.average
            awl = aw/al
            lw = tt.streak.won.longest
            ll = tt.streak.lost.longest
            rtlist.append(rt)
            rtrank = ss.rankdata([-1 * i for i in rtlist])
            maxdnlist.append(dd.max.drawdown)
            mdnrank = ss.rankdata(maxdnlist)
            wtlist.append(wt)
            wtrank = ss.rankdata([-1 * i for i in wtlist])  
            awllist.append(awl)
            awlrank = ss.rankdata(awllist)
            final_results_list.append(['SMACross', strategy.params.pfast, 
                strategy.params.pslow, round(rt,4), round(dd.max.drawdown,4), round(tt.total.closed,4), round(tt.won.total,4), round(tt.lost.total,4), round(wt,4), round(aw,4), round(al,4), round(lw,4), round(ll,4), round(-awl,4)])

    df = pd.DataFrame(final_results_list, columns=['Name','sma_pfast','sma_pslow','Return','MaxDrawDown','TotalTrades#','WinTrades#','LossTrades#','WinRatio','AverageWin$','AverageLoss$','LongestWinStreak','LongestLossStreak','AverageWinLossRatio'])
    df['RankReturn'] = rtrank
    df['RankMaxdrawdown'] = mdnrank
    df['RankWinRatio'] = wtrank
    df['RankAverageWinLossRatio'] = awlrank
    df['Score'] = df[['RankReturn', 'RankMaxdrawdown', 'RankWinRatio', 'RankAverageWinLossRatio']].mean(1)
    df.to_csv(logdir+'BTC_USDT_SMACross.csv', sep=',')



