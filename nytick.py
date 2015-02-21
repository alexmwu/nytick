from flask import Flask

from news.nyapi.topstories import NyTop


# Application: stachacks
NY_TOPSTORIES_KEY = '976d33d544c93cac3d4c4f3fc55017d6:19:71402826'

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

if __name__ == '__main__':
    app.run()
