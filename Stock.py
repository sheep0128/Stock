import pandas.io.data as web
import datetime
import pandas
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


def main():
    kb = Series([37500, 36350, 38100, 37950, 37200, 36800])
    print(kb)
    data = dict(foreigner=[603105, -405885, 283715, 365410, 302876, 393534],
                sratio=[69.15, 68.99, 69.09, 69.02, 68.93, 68.85],
                org=[-175461, -491416, -103877, -66765, -200711, -356901],
                sprice=[37500, 36350, 38100, 37950, 37200, 36800], fluctuation=[3.16, -4.59, 0.40, 2.02, 1.09, -0.67])
    frame = DataFrame(data)
    print(frame)
    frame3 = DataFrame(data, columns=['foreigner', 'sratio', 'org', 'sprice', 'fluctuation'],
                       index=['02.06', '02.05', '02.04', '02.03', '02.02', '01.30'])
    print(frame3)
    start = datetime.datetime(2015, 2, 2)

    end = datetime.datetime(2015, 2, 13)
    gs = web.DataReader("078930.KS", "yahoo", start, end)
    print(gs)

    plt.plot(gs.index, gs['Close'])
    plt.show()

if __name__ == "__main__":
    main()
