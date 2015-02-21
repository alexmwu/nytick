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
    data = api.daily_popular_stories()
    print str(data)
    return str(data)

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
    if APP_TYPE=='console':
        main()
    elif APP_TYPE=='web':
        app.debug=True
        app.run()
    else:
        print "Error -", APP_TYPE
