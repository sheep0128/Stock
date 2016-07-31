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

    date_list = []
    #stockInfo = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
    stockInfo = pd.DataFrame(columns=['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
    # first = datetime.date(2016, 1, 1)
    # date_list.append(first)
    # stock = Series(
    #     [float(0),
    #      float(0),
    #      float(0),
    #      float(0),
    #      int(0),
    #      float(0)],
    #     index=['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
    # stockInfo = stockInfo.append(stock, ignore_index=True)

    #for page in range(1, mpNum + 1):
    for page in range(1, 6):
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
                date_list.append(srlists[i].find_all("td", align="center")[0].text);

                if (int(srlists[i].find_all("td", class_="num")[5].text.replace(',', '')) == 0):
                    stock = Series(
                        [float(srlists[i].find_all("td", class_="num")[0].text.replace(',', '')),
                         float(srlists[i].find_all("td", class_="num")[0].text.replace(',', '')),
                         float(srlists[i].find_all("td", class_="num")[0].text.replace(',', '')),
                         float(srlists[i].find_all("td", class_="num")[0].text.replace(',', '')),
                         int(srlists[i].find_all("td", class_="num")[5].text.replace(',', '')),
                         float(srlists[i].find_all("td", class_="num")[0].text.replace(',', ''))],
                        index=['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
                else:
                    stock = Series(
                        [float(srlists[i].find_all("td", class_="num")[2].text.replace(',', '')),
                         float(srlists[i].find_all("td", class_="num")[3].text.replace(',', '')),
                         float(srlists[i].find_all("td", class_="num")[4].text.replace(',', '')), float(srlists[i].find_all("td", class_="num")[0].text.replace(',', '')),
                         int(srlists[i].find_all("td", class_="num")[5].text.replace(',', '')), float(srlists[i].find_all("td", class_="num")[0].text.replace(',', ''))],
                        index=['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])
                stockInfo = stockInfo.append(stock, ignore_index=True)


                # print(srlists[i].find_all("td", align="center")[0].text,
                #       srlists[i].find_all("td", class_="num")[0].text, srlists[i].find_all("td", class_="num")[5].text)

    stockInfo.set_index(pd.DatetimeIndex(date_list), inplace=True)
    stockInfo.sort_index(inplace=True, ascending=True)
    return stockInfo
