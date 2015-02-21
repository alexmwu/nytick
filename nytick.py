from flask import Flask

from news.nyapi import NY_TOPSTORIES_KEY
from news.nyapi.topstories import NyTop

APP_TYPE = 'console'

# Application: stachacks

app = Flask(__name__)

@app.route('/top')
def show_top_stories():
    api = NyTop(NY_TOPSTORIES_KEY)
    data = api.top_stories()
    print data['num_results'] # example data access
    return str(data)

@app.route('/')
def hello_world():
    return 'Hello World!'

def main():
    from bloomberg import ticks
    ticks.get_historical_data()

if __name__ == '__main__':
    if APP_TYPE=='console':
        main()
    else:
        app.run()
