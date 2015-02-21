from bs4 import BeautifulSoup
import requests

org_names = ["facebook","WALMART STORES INC","st andrews"]
for org in org_names:
    print "Organisation name: "+org
    r = requests.get("https://www.google.com/finance?q="+org.replace(" ","+"))
    soup = BeautifulSoup(r.text)
    text = str(soup.find_all("div", class_="fjfe-content"))
    start = text.find("var _ticker = ") # comes before the ticker symbol name
    if start==-1:   # if not found
        print "Not a company error"
    else:
        end = text.find("';",start)
        stock_symbol = text[start+15:end]   # saved as market:symbol
        print stock_symbol