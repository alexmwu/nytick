from unittest import TestCase
import bloomberg.ticks

__author__ = 'dewaka'

class TestRequest_ticker(TestCase):
    def test_request_ticker(self):
        data = bloomberg.ticks.request_ticker("GOOG US Equity"
                                              "bloomberg.crt",
                                              "/home/dewaka/client.crt",
                                              "/home/dewaka/client.key")
        assert True
