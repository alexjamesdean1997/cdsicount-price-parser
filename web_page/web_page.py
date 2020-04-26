from flask import Flask, request, render_template
from cdiscount.price_parser import parse_price

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def webpage():
    if request.method =='GET':
        return render_template('index.html')
    elif request.method =='POST':
        sku = request.form['sku']
        price = {"price": parse_price(sku)}
        return render_template('result.html', **price)


if __name__ == "__name__":
    app.run(ssl_context='adhoc')























# import urllib.request
# import urllib.parse
# import re
# from flask import Flask, request, render_template
#
# app = Flask(__name__)
#
# @app.route('/', methods=['POST', 'GET'])
# def webpage():
#     if request.method =='GET':
#         return render_template('index.html')
#     elif request.method =='POST':
#         sku = request.form['sku']
#         url = 'https://www.cdiscount.com/f-0-'
#         skuurl = url + sku + '.html'
#         req = urllib.request.Request(skuurl)
#         resp = urllib.request.urlopen(req)
#         respData = resp.read()
#         getprice = re.findall(r'"price":(.*?),', str(respData))
#         price = {"price": float(getprice[0])}
#         return render_template('result.html', **price)
#
#
# if __name__ == "__name__":
#     app.run(ssl_context='adhoc')