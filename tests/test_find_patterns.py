import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from stock_requests import stock
from helper import stock_patterns

print "Beginning test with AAPL stock"

aapl = stock.Stock('aapl')

print "Finding doji..."
stock_patterns.find_doji(aapl)
print "Dojis found:   ", len(aapl.doji_dates)
print "Finding bullish..."
stock_patterns.find_bullish_engulfing(aapl)
print "Bullish found:    ", len(aapl.bullish_engulfing_dates)
print "Finding bearish..."
stock_patterns.find_bearish_engulfing(aapl)
print "Bearish found:    ", len(aapl.bearish_engulfing_dates)