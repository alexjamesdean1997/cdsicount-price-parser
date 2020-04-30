from flask import Flask, request, render_template
from cdiscount.price_parser import parse_price

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def webpage():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        sku = request.form['sku']
        price = {"price": parse_price(sku)}
        return render_template('result.html', **price)


if __name__ == "__name__":
    app.run(ssl_context='adhoc')
