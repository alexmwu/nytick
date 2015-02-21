from unittest import TestCase
import ticker_fetch

__author__ = 'dewaka'

class TestFetch_ticker_symbol(TestCase):
    def test_fetch_ticker_symbol_google(self):
        symbol = ticker_fetch.fetch_ticker_symbol("Google")
        assert symbol != []
        self.assertEqual(symbol[1], 'GOOGL')
        self.assertEqual(symbol[0], 'NASDAQ')

    def test_fetch_ticker_symbol_apple(self):
        symbol = ticker_fetch.fetch_ticker_symbol("Apple")
        assert symbol != []
        self.assertEqual(symbol[1], 'AAPL')
        self.assertEqual(symbol[0], 'NASDAQ')

    def test_fetch_ticker_symbol_empty(self):
        symbol = ticker_fetch.fetch_ticker_symbol("St Andrews")
        assert symbol == []
