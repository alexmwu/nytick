from flask import Flask,render_template

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
    for k in sinfo.keys():
        data = ticks.request_ticker("{} US Equity".format(sinfo[k]))
        #print data
        return data

@app.route('/popular')
def show_popular_stories():
    api = NyTimes()
    data = api.daily_popular_stories(0)
    #print str(data)
    
    for article in data['results']:
        symbols, pub_date = grab_tickers(article)
        #print pub_date
        print "#################"
        print symbols
        print "################"
        print pub_date
        print "*****************"
        get_stock_data(symbols)
    return str(data)

def get_popular_stocks():
    api = NyTimes()
    data = api.daily_popular_stories(0)
    
    stocks=[]

    for article in data['results']:
        symbols, pub_date = grab_tickers(article)
        stock = get_stock_data(symbols)
        print stock
        stocks.append(stock)
    return stocks

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

@app.route('/')
def index(name=None):
    stocks = get_popular_stocks()
    return render_template('c3test.html', stocks=stocks)

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
            #app.debug=True
            #app.run(host='0.0.0.0')
            get_popular_stocks()
        elif APP_TYPE=='console':
            main()
        else:
            print "Error AppType:", APP_TYPE
