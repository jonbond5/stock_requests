from get_av_key import get_av_key
import requests as r
import json

global base_url 
base_url = "https://www.alphavantage.co/query?function={}&symbol={}&apikey="+get_av_key()
def build_time_series_url(function, symbol):
    """
    Build AV url for any inter-day time series query (intra day NOT supported)
    """
    return base_url.format(function, symbol)

def build_ticker_query(keyword):
    """
    Find ticker closest to keyword given (e.g.: build_ticker_query('boe') --> "Boeing", etc.)
    """
    return base_url.replace("symbol", "keywords").format("SYMBOL_SEARCH", keyword)



def get_query_results(url):
    """
    Execute query results and transform response into JSON
    """
    query_results = r.get(url).content.replace("\n","").replace(" ","")
    return json.loads(query_results)
