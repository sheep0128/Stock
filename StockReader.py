import datetime
import urllib
import time
from pandas import Series, DataFrame
import pandas as pd

from urllib.request import urlopen
from bs4 import BeautifulSoup


def getStockItem(stockItem):
    url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem
    html = urlopen(url)
    source = BeautifulSoup(html.read(), "html.parser")

    maxPage = source.find_all("table", align="center")
    mp = maxPage[0].find_all("td", class_="pgRR")
    mpNum = int(mp[0].a.get('href')[-3:])

    stockInfo = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])

    #for page in range(1, mpNum + 1):
    for page in range(1, 3):
        print(str(page))
        url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem + '&page=' + str(page)
        html = urlopen(url)
        source = BeautifulSoup(html.read(), "html.parser")
        srlists = source.find_all("tr")
        isCheckNone = None

        # if ((page % 1) == 0):
        # time.sleep(1.50)

        for i in range(1, len(srlists) - 1):
            if (srlists[i].span != isCheckNone):
                srlists[i].td.text
                # stock = [
                #    [srlists[i].find_all("td", align="center")[0].text, srlists[i].find_all("td", class_="num")[2].text, srlists[i].find_all("td", class_="num")[3].text,
                #     srlists[i].find_all("td", class_="num")[4].text, srlists[i].find_all("td", class_="num")[0].text,
                #     srlists[i].find_all("td", class_="num")[5].text, srlists[i].find_all("td", class_="num")[0].text]]
                stock = Series(
                    [srlists[i].find_all("td", align="center")[0].text, float(srlists[i].find_all("td", class_="num")[2].text.replace(',','')),
                     float(srlists[i].find_all("td", class_="num")[3].text.replace(',', '')),
                     float(srlists[i].find_all("td", class_="num")[4].text.replace(',','')), float(srlists[i].find_all("td", class_="num")[0].text.replace(',','')),
                     int(srlists[i].find_all("td", class_="num")[5].text.replace(',','')), float(srlists[i].find_all("td", class_="num")[0].text.replace(',',''))],
                    index=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
                stockInfo = stockInfo.append(stock, ignore_index=True)


                # print(srlists[i].find_all("td", align="center")[0].text,
                #       srlists[i].find_all("td", class_="num")[0].text, srlists[i].find_all("td", class_="num")[5].text)

    stockInfo.set_index(pd.DatetimeIndex(stockInfo['Date']), inplace=True)
    stockInfo.sort_index(inplace=True, ascending=True)
    print(stockInfo)
    return stockInfo
