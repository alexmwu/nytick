from bs4 import BeautifulSoup
import requests

common_tickers = {}

def fetch_ticker_symbol(name):

    if common_tickers.has_key(name):
        return common_tickers[name]

    req = requests.get("https://www.google.com/finance?q=" + name.replace(" ", "+"))
    soup = BeautifulSoup(req.text)
    text = str(soup.find_all("div", class_="fjfe-content"))

    if text:
        start = text.find("var _ticker = ") # comes before the ticker symbol name
        if start==-1:   # if not found
            return []
        else:
            end = text.find("';",start)
            stock_symbol = text[start+15:end]   # saved as market:symbol
            if not stock_symbol.strip():    # sometimes stock_symbol can be whitespace
                return []

            info = stock_symbol.split(":")
            common_tickers[name] = info

            return info
    else:
        common_tickers[name] = []
        return []

def test_ticker_fetch():
    org_names = ["facebook","WALMART STORES INC","st andrews", "Morgan stanley", "american express "]
    for org in org_names:
        ticker_symbol = fetch_ticker_symbol(org)

        if ticker_symbol==[]:
            print 'Failed to fetch symbol for:', org
        else:
            print org, ' Symbol:', ticker_symbol[1], ', Market:', ticker_symbol[0]

