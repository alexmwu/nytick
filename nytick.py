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

@app.route('/popular_stories')
def popular_stories():
    api = NyTimes()
    data = api.daily_popular_stories(0)
    return json.dumps(data)

@app.route('/get_stocks/<symbol>')
def get_stocks_for_symbol(symbol):
    print 'get_stocks_for_symbol:', symbol
    data = []
    if symbol is not None:
        data = ticks.request_ticker("{} US Equity".format(symbol))
    print data
    return json.dumps(data)

# Returns a JSON array of most popular stories
@app.route('/')
def index(name=None):
    # stocks = parse_stock_data(get_popular_stocks()[0]) #will only do for first stock data

    api = NyTimes()
    p_stories = api.daily_popular_stories(0)

    print p_stories

    articles = []
    for article in p_stories["results"]:
        info = {}
        symbols, pub_date = grab_tickers(article)
        if pub_date == -1:
            info['is_ticker'] = False
            info['symbols'] = []
        else:
            info['is_ticker'] = True
            info['symbols'] = symbols
        info['data'] = article
        articles.append(info)

    return render_template('c3test.html', popular_stories=json.dumps(articles))
>>>>>>> c81ad7baea5226bd2be1ec15f44607c48624cd5a

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
