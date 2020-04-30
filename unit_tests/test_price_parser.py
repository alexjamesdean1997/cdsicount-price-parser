import unittest
from cdiscount.price_parser import parse_price


class TestParsePrice(unittest.TestCase):

    def test_parse_price(self):
        # Test when sku is a string, expect float
        self.assertEqual(type(parse_price("del5397184246030")), float)

        # Tests when sku is not a string, expect False
        self.assertFalse(parse_price(42), False)
        self.assertFalse(parse_price(3.14), False)
        self.assertFalse(parse_price([1, 2, 3, 4]), False)
        self.assertFalse(parse_price(True), False)
        self.assertFalse(parse_price(False), False)
