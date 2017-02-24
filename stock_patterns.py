from stock import Stock

with open('stock_symbol_list.csv') as f:
    stock_list = f.read().split(',')

# total_requests = 0
# 
# for elem in stock_list:
#     total_requests += 1
#     try:
#         stock = Stock(elem,debug=True)
#     except Exception as e:
#         print "Failed after: ", total_requests
#         break

def find_doji(stock):
    """
    Pass in stock object

    Returns a list of dates where a doji occurred
    """
    doji_scale = 0.05 # Percentage of how close closes and opens of a given day must be
    c = stock.closes
    o = stock.opens
    # Traverse opens and closes
    # If the close is within doji_scale of open, add that DATE to the list
    stock.doji_dates = [stock.dates[x] for x in range(len(stock.closes)) if c[x] / o[x] < doji_scale and c[x]/o[x] > doji_scale]
    return

def find_bullish_engulfing(stock, bull_scale=0.1):
    """
    Pass in stock object

    Returns a list of dates where bullish engulfing occurs
    """
    c = stock.closes
    o = stock.opens
    stock.bullish_engulfing_dates = [stock.dates[x] for x in range(len(c)) if c[x] / o[x] >= bull_scale]
    return

def find_bearish_engulfing(stock, bear_scale=0.1):
    c = stock.closes
    o = stock.opens
    stock.bearish_engulfing_dates = [stock.dates[x] for x in range(len(c)) if c[x] / o[x] <= bull_scale]
    return