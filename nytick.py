from flask import Flask,render_template

from news.nyapi.topstories import NyTimes

APP_TYPE = 'console'

app = Flask(__name__)

@app.route('/top')
def show_top_stories():
    api = NyTimes()
    data = api.top_stories()
    print data['num_results'] # example data access
    return str(data)

@app.route('/popular')
def show_popular_stories():
    api = NyTimes()
    data = api.daily_popular_stories(0)
    #print str(data)
    
    for article in data['results']:
        grab_tickers(article)
    return str(data)

def grab_tickers(article):
    # Grabs the organisation names and returns lists of the ticker symbols and markets
    import ticker_fetch
    organisations = article['org_facet']
    symbols = []
    markets = []
    print "**",article['title'],"**"
    if len(organisations)>0:
        #print "**",article['title'],"**"    # print article title
        for organisation in organisations:
            symbol = ticker_fetch.fetch_ticker_symbol(organisation)
            if symbol==[]:
                print 'Failed to fetch symbol for:',organisation
            else:
                symbols.append(symbol[1])   # add to the lists
                markets.append(symbol[0])
    return symbols,markets

@app.route('/')
def index(name=None):
    return render_template('c3test.html', name=name)

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
            app.run()
        elif APP_TYPE=='console':
            main()
        else:
            print "Error AppType:", APP_TYPE
