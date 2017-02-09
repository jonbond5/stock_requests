import requests as r
import pandas as pd
from StringIO import StringIO as SIO
import json

req = r.get('http://www.nasdaq.com/screening/companies-by-industry.aspx?NASDAQ&render=download')
data = pd.read_csv(SIO(req.text))

cleaned = [x for x in data['Symbol'].tolist() if x.find('^') ==-1]

with open('stock_symbol_list.csv','w') as f:
    f.write(','.join(cleaned).replace(' ',''))