__author__ = 'dewaka'

import news.nyapi
import requests

API_INFO = {
    "top_stories": {
        "api_root" : 'http://api.nytimes.com/svc/topstories/v1/home.{0}?api-key={1}',
        "api_key": news.nyapi.NY_TOPSTORIES_KEY },
    "popular_stories": {
        "api_root" : 'http://api.nytimes.com/svc/mostpopular/v2/mostviewed/Business%20Day/1.{0}?api-key={1}',
        "api_key": news.nyapi.NY_POPULARSTORIES_KEY }
}

class NyTimes:
    def __init__(self):
        self.FORMAT = 'json'

    def _topstories_api(self):
        api = API_INFO['top_stories']
        return api['api_root'].format(self.FORMAT, api["api_key"])

    def _popular_stories_api(self):
        api = API_INFO['top_stories']
        return api['api_root'].format(self.FORMAT, api["api_key"])

    def daily_popular_stories(self, **kwargs):
        req = requests.get(self._popular_stories_api())
        print req
        return req.json()

    def top_stories(self, **kwargs):
        req = requests.get(self._topstories_api())
        return req.json()
