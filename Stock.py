import pandas_datareader.data as web
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.finance as matfin
import matplotlib.ticker as ticker
import StockReader

def main():
    #start = datetime.datetime(2016, 3, 1)
    #end = datetime.datetime(2016, 3, 31)
    #skhynix = web.DataReader("078930.KS", "yahoo", start, end)

    stockInfo = StockReader.getStockItem("026260").tail(30)

    stockInfo['MA5'] = stockInfo['Adj Close'].rolling(window=5).mean()
    stockInfo['MA20'] = stockInfo['Adj Close'].rolling(window=20).mean()
    stockInfo['MA60'] = stockInfo['Adj Close'].rolling(window=60).mean()
    stockInfo['MA120'] = stockInfo['Adj Close'].rolling(window=120).mean()
    #print(stockInfo)
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(311)

    day_list = []
    name_list = []

    for i, day in enumerate(stockInfo.index):
        #if day.dayofweek == 0:
            day_list.append(i)
            name_list.append(day.strftime('%d'))
            #name_list.append(day.strftime('%Y-%m-%d') + '(Mon)')
        #else:
        #    print(day.weekday())


    print(day_list)
    print(name_list)

    ax.text(.5, .9, 'centered title',
            horizontalalignment='center',
            transform=ax.transAxes)
    ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))

    matfin.candlestick2_ohlc(ax, stockInfo['Open'], stockInfo['High'], stockInfo['Low'], stockInfo['Close'], width=0.5,
                             colorup='r', colordown='b')
    plt.grid()
    print(stockInfo['Volume'])

    ax = fig.add_subplot(312)
    ax.bar(stockInfo['Volume'].index, stockInfo['Volume'], width=0.8)
    plt.grid()


    plt.figure(1)
    plt.subplot(313)
    plt.plot(stockInfo.index, stockInfo['MA5'], label="MA5")
    plt.plot(stockInfo.index, stockInfo['MA20'], label="MA20")
    plt.plot(stockInfo.index, stockInfo['MA60'], label="MA60")
    #plt.plot(stockInfo.index, stockInfo['MA120'], label="MA120")
    plt.legend(loc='best')

    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()

# import pandas_datareader.data as web
# import datetime
# import matplotlib.pyplot as plt
# import matplotlib.finance as matfin
# import matplotlib.ticker as ticker
#
# start = datetime.datetime(2016, 3, 1)
# end = datetime.datetime(2016, 3, 31)
# skhynix = web.DataReader("000660.KS", "yahoo", start, end)
# #skhynix = skhynix[skhynix['Volume'] > 0]
#
# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(111)
#
# day_list = range(len(skhynix))
# name_list = []
# for day in skhynix.index:
#     name_list.append(day.strftime('%d'))
#
# print(day_list)
# print(name_list)
# ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
# ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))
#
# matfin.candlestick2_ohlc(ax, skhynix['Open'], skhynix['High'], skhynix['Low'], skhynix['Close'], width=0.5, colorup='r', colordown='b')
# plt.show()