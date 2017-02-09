import requests as req
import pandas as pd
from custom_exceptions import HTTPError
from StringIO import StringIO as SIO
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

class Stock:
    """
    Object that contains info for a given stock
    """

    def __init__(self, symbol):
        self.stock_symbol = symbol
        self.url = self.generate_url(self.stock_symbol)
        self.csv_data = self.getHistory(self.url)
        self.parse_data(self.csv_data)
        return

    def generate_url(self, symbol):
        """
        Given a stock symbol, return the Google Finance url for said stock
        """
        return "http://www.google.com/finance/historical?q=NASDAQ\%3A{}&ei=iG58WJnjBtbBeoawvugI&output=csv".format(symbol.upper())

    def getHistory(self, url):
        history_request = req.get(url)
        print "Status code:  ", history_request.status_code
        # Check if url exist
        if history_request.status_code >= 400:
            raise HTTPError("The stock requested is unvailable.  Google responded with code {}".format(str(history_request.status_code) + " when given stock " + symbol.upper() + ".  URL is " + url))

        self.data = history_request.text
        return history_request.text

    def parse_data(self, data):
        """
        Creates global variable 'data' that holds each column of stock data in a dict.
        Column options:
            -Date, Open, Close, High, Low, Volume
        """
        self.data = pd.read_csv(SIO(data))
        self.opens = self.data['Open']
        self.closes = self.data['Close']
        self.dates = self.data['Date']
        self.highs = self.data['High']
        self.lows = self.data['Low']
        self.volumes = self.data['Volume']
        return

    def reverse_data(self, data):
        data = data.tolist()
        data.reverse()
        return data

    def graph_data(self, option='Close'):
        data = self.data
        x_axis = self.dates
        if option != 'Date':
            y_axis = self.reverse_data(data[option])
        else:
            print 'Very funny...'
            return
        plt.plot(y_axis)
        plt.ylabel("Cost / Share")
        plt.show()
        return

    def predict_good_bad(self):
        to_review = self.closes.tolist()
        to_review = to_review[-20:]
        if to_review[0] > to_review[19]:
            return 'good'
        else:
            return 'bad'

def mass_prediction():
    good_list = []
    with open('stock_symbols.csv') as f:
        for row in f:
            symbol = row.strip('\n')
            print "Starting......", symbol
            try:
                stock = Stock(symbol)
            except (HTTPError, NameError):
                continue
            if stock.predict_good_bad() == 'good':
                good_list.append(stock)
    return good_list