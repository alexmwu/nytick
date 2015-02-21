__author__ = 'dewaka'

import json
import ssl
import urllib2
import datetime

import bloomberg


data = {
    "securities": ["WMT US Equity"],
    "fields": ["PX_LAST", "OPEN", "EPS_ANNUALIZED"],
    "startDate": "20120101",
    "endDate": "20120301",
    "periodicitySelection": "DAILY"
}

def _ticker_request(request_data):
    req = urllib2.Request(
        'https://{}/request?ns=blp&service=refdata&type=HistoricalDataRequest'.format(bloomberg.API_HOST))
    req.add_header('Content-Type', 'application/json')

    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_verify_locations('bloomberg.crt')
    ctx.load_cert_chain('client.crt', 'client.key')

    try:
        res = urllib2.urlopen(req, data=json.dumps(request_data), context=ctx)
        return res.read()
    except Exception as e:
        print e
        return None

def _month_earlier():
    month_early = datetime.datetime.now() - datetime.timedelta(days=30)
    return month_early.strftime("%Y%m%d")

def _today():
    return datetime.datetime.now().strftime("%Y%m%d")

def request_ticker(sec_name, **kwargs):
    kwargs["securities"] = [sec_name]
    if "fields" not in kwargs:
        kwargs["fields"] = ["PX_LAST", "OPEN", "EPS_ANNUALIZED"]
    if "startDate" not in kwargs:
        kwargs["startDate"] = _month_earlier()
    if "endDate" not in kwargs:
        kwargs["endDate"] = _today()
    if "periodicitySelection" not in kwargs:
        kwargs["periodicitySelection"] = "DAILY"

    return _ticker_request(kwargs)

def request(host):
    req = urllib2.Request('https://{}/request?ns=blp&service=refdata&type=HistoricalDataRequest'.format(host))
    req.add_header('Content-Type', 'application/json')

    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_verify_locations('bloomberg.crt')
    ctx.load_cert_chain('client.crt', 'client.key')

    try:
        res = urllib2.urlopen(req, data=json.dumps(data), context=ctx)
        print res.read()
    except Exception as e:
        print e
        return 1
    return 0


def test_request():
    print _ticker_request({
        "securities": ["WMT US Equity"],
        "fields": ["PX_LAST", "OPEN", "EPS_ANNUALIZED"],
        "startDate": "20120101",
        "endDate": "20120301",
        "periodicitySelection": "DAILY"
    })
    print request_ticker("WMT US Equity")

def get_historical_data():
    test_request()
    print 'in historical data'
