import urllib.request
import urllib.parse
import re


def parse_price(sku):
    if isinstance(sku, str):
        url = 'https://www.cdiscount.com/f-0-'
        skuurl = url + sku + '.html'
        req = urllib.request.Request(skuurl)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        getprice = re.findall(r'"price":(.*?),', str(respData))
        price = float(getprice[0])
        return price
    else:
        return False
