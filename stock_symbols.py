import requests as r
import pandas as pd
from StringIO import StringIO as SIO
import json

base = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?'
exchanges = ['NASDAQ', 'NYSE', 'AMEX']
sources = [base+"{}".format(y)+"&render=download" for y in exchanges]

for url in sources:
    print url
    print r.get(url).text

# index = 0
# for url in sources:
#     file = r.get(url)
#     with open(exchanges[index]+".csv", 'w') as f:
#         f.write(','.join(pd.read_csv(SIO(file.text))['Symbol']))
#     index += 1