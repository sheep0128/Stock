import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import matplotlib.finance as matfin
import matplotlib.ticker as ticker
import StockReader

def main():
    #start = datetime.datetime(2016, 3, 1)
    #end = datetime.datetime(2016, 3, 31)
    #skhynix = web.DataReader("078930.KS", "yahoo", start, end)

    stockInfo = StockReader.getStockItem("040350").tail(10)

    print(stockInfo.index[0])
    print(stockInfo.dtypes)
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)

    day_list = []
    name_list = []
    for i, day in enumerate(stockInfo.index):
        if day.dayofweek == 0:
            day_list.append(i)
            name_list.append(day.strftime('%Y-%m-%d') + '(Mon)')

    ax.xaxis.set_major_locator(ticker.FixedLocator(day_list))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(name_list))

    matfin.candlestick2_ohlc(ax, stockInfo['Open'], stockInfo['High'], stockInfo['Low'], stockInfo['Close'], width=0.5,
                             colorup='r', colordown='b')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
