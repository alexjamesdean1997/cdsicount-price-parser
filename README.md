# Cdiscount price parser

This python package allows you to get the price of any Cdiscount article with the reference number of the product.


## Getting started

1. Open your command-line text editor and change your directory to the cdiscount package
```
cd <path>/cdiscount-price-parser
```

2. Run Python
```
python
```

3. Import the parse_price method from the price_parser module
```
>>> from cdiscount.price_parser import parse_price
```

4. Assign your product identifier value to a variable
```
>>> sku = "<your-product-id>"
```

5. Call the parse_price method with your variable
```
>>> parse_price(sku)
```

This will return the price of your product


## Author

Alexandre Dean