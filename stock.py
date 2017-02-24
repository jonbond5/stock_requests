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

    def __init__(self, symbol,debug=False):
        self.symbol = symbol
        self.url = self.generate_url(self.symbol)
        self.csv_data, self.code = self.getHistory()
        if self.code >= 400:
            pass
        else:
            self.parse_data(self.csv_data)
        return

    def generate_url(self, symbol):
        """
        Given a stock symbol, return the Google Finance url for said stock
        """
        return "http://www.google.com/finance/historical?q=NASDAQ\%3A{}&ei=iG58WJnjBtbBeoawvugI&output=csv".format(symbol.upper())

    def getHistory(self):
        history_request = req.get(self.url)
        print "Status code:  ", history_request.status_code, " with ", self.symbol
        # Check if url exist
        if history_request.status_code >= 500:
            raise HTTPError("The stock requested is unvailable.  Google responded with code {}".format(str(history_request.status_code) + " when given stock " + self.symbol.upper() + ".  URL is " + self.url))
        self.data = history_request.text
        return history_request.text, history_request.status_code

    def parse_data(self, data):
        """
        Creates global variable 'data' that holds each column of stock data in a dict.
        Column options:
            -Date, Open, Close, High, Low, Volume
        """
        self.data = pd.read_csv(SIO(data))
        self.opens = self.data['Open'].tolist()
        self.closes = self.data['Close'].tolist()
        self.dates = self.data['Date'].tolist()
        self.highs = self.data['High'].tolist()
        self.lows = self.data['Low'].tolist()
        self.volumes = self.data['Volume'].tolist()
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
