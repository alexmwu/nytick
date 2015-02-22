from flask import Flask,render_template,Markup
import json
from news.nyapi.topstories import NyTimes
from bloomberg import ticks

APP_TYPE = 'web'

app = Flask(__name__)

@app.route('/top')
def show_top_stories():
    api = NyTimes()
    data = api.top_stories()
    #print data['num_results'] # example data access
    return str(data)


def get_stock_data(sinfo):
    data=[]
    for k in sinfo.keys():
        data = ticks.request_ticker("{} US Equity".format(k))
        #print data
        return data

@app.route('/popular')
def show_popular_stories():
    api = NyTimes()
    data = api.daily_popular_stories(0)
    return str(data)

def get_popular_stocks():
    api = NyTimes()
    data = api.daily_popular_stories(0)
    
    stocks=[]

    for article in data['results']:
        symbols, pub_date = grab_tickers(article)
        if(pub_date!=-1):
            #print symbols,pub_date     
            stock = get_stock_data(symbols)
            #print stock
            stocks.append(stock)
    return stocks

#returns array of stock info requested in bloomberg HTTP api
def parse_stock_data(stock):
    stock_json = json.loads(stock)
    #print stock_json
    data = stock_json["data"][0]
    #print data
    securityData = data["securityData"]
    #print securityData
    fieldData = securityData["fieldData"]
    #print fieldData
    return fieldData
    

def grab_tickers(article):
    # Grabs the organisation names and returns lists of the ticker symbols and markets
    import ticker_fetch
    organisations = article['org_facet']
    symbols = {}
    pub_date = -1
    #print "**",article['title'],"**"
    if len(organisations)>0:
        #print "**",article['title'],"**"    # print article title
        for organisation in organisations:
            symbol = ticker_fetch.fetch_ticker_symbol(organisation)
            if symbol!=[]:
            #     print 'Failed to fetch symbol for:',organisation
            # else:
                # symbols.append(symbol[1])   # add to the lists
                symbols[symbol[1]] = symbol[0]
                pub_date = article['published_date']
            
    return symbols, pub_date

#format stocks array into json for correct passing into javascript
def stocks_to_js(stocks):
    output={}
    for i in range(0,len(stocks)):
        #print stocks[i] 
        output[str(i)] = stocks[i] 
    return output

@app.route('/')
def index(name=None):
    stocks = parse_stock_data(get_popular_stocks()[0]) #will only do for first stock data
    stocks=stocks_to_js(stocks)
    stocks = str(stocks) 
    return render_template('c3test.html',stocks=json.dumps(stocks))

def main():
    # from bloomberg import ticks
    # ticks.get_historical_data()
    # import ticker_fetch
    # print ticker_fetch.test_ticker_fetch()
    # print show_popular_stories()
    show_top_stories()
    show_popular_stories()

if __name__ == '__main__':
        if APP_TYPE=='web':
            app.debug=True
            app.run(host='0.0.0.0')
        elif APP_TYPE=='console':
            main()
        else:
            print "Error AppType:", APP_TYPE
