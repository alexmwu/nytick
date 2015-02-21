__author__ = 'dewaka'

import news.nyapi
import requests

API_INFO = {
    "top_stories": {
        "api_root" : 'http://api.nytimes.com/svc/topstories/v1/home.{0}?api-key={1}',
        "api_key": news.nyapi.NY_TOPSTORIES_KEY },
    "popular_stories": {
        "api_root" : 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/Business%20Day/1.{0}?offset={2}&api-key={1}',
        "api_key": news.nyapi.NY_POPULARSTORIES_KEY }
}

class NyTimes:
    def __init__(self):
        self.FORMAT = 'json'

    def _topstories_api(self):
        api = API_INFO['top_stories']
        return api['api_root'].format(self.FORMAT, api["api_key"])

    def _popular_stories_api(self, offset):
        api = API_INFO['top_stories']
        return api['api_root'].format(self.FORMAT, api["api_key"], offset)

    def daily_popular_stories(self, offset, **kwargs):
        #req = requests.get(self._popular_stories_api(offset))
        req = requests.get("http://api.nytimes.com/svc/mostpopular/v2/mostviewed/Business%20Day/1.json?offset=0&api-key=29e8d673b8ad9bf010bfbb409fc06398%3A8%3A66957850")
        print req.text
        return req.json()

	

    def top_stories(self, **kwargs):
        req = requests.get(self._topstories_api())
        return req.json()
