__author__ = 'dewaka'

import json
import ssl
import urllib2

data = {
    "securities": ["WMT US Equity"],
    "fields": ["PX_LAST", "OPEN", "EPS_ANNUALIZED"],
    "startDate": "20120101",
    "endDate": "20120301",
    "periodicitySelection": "DAILY"
}


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
    import bloomberg
    print request(bloomberg.API_HOST)

def get_historical_data():
    test_request()
    print 'in historical data'
