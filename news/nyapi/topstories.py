__author__ = 'dewaka'

import requests

TOPSTORIES_API_ROOT = 'http://api.nytimes.com/svc/topstories/v1/home.{0}?api-key={1}'

class NyTop:
    def __init__(self, api_key):
        self.API_KEY = api_key
        self.FORMAT = 'json'

    def _get_api(self):
        return TOPSTORIES_API_ROOT.format(self.FORMAT, self.API_KEY)

    def top_stories(self, **kwargs):
        req = requests.get(self._get_api())
        return req.json()
