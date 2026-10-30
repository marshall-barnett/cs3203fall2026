import unittest
import sys

# Minimal implementation of the PriceSort functions for testing purposes
BOOKS = [
    {"title": "Calculus: Early Transcendentals", "price": 89.99},
    {"title": "Introduction to Algorithms", "price": 65.50},
    {"title": "Computer Organization and Design", "price": 45.00},
]

def fetchPrice(price):
    if not isinstance(price, float):
        return []
    return [book["title"] for book in BOOKS if book["price"] <= price]

def fetchTitleKeyword(keyword):
    if not isinstance(keyword, str) or keyword.strip() == "" or len(keyword) > 255:
        return []
    return [book["title"] for book in BOOKS if keyword.lower() in book["title"].lower()]

# Unit tests for the PriceSort functions

class TestPriceSort(unittest.TestCase):

    # Unit1: fetchPrice(float price)
    def test_valid_price(self):
        result = fetchPrice(50.0)
        self.assertEqual(result, ["Computer Organization and Design"])

    def test_invalid_price(self):
        result = fetchPrice("fifty")
        self.assertEqual(result, [])

    def test_boundary_max_float(self):
        result = fetchPrice(sys.float_info.max)
        self.assertEqual(len(result), 3)

    def test_edge_no_books_below_price(self):
        result = fetchPrice(10.0)
        self.assertEqual(result, [])

    # Unit2: fetchTitleKeyword(String keyword)
    def test_valid_keyword(self):
        result = fetchTitleKeyword("Calculus")
        self.assertEqual(result, ["Calculus: Early Transcendentals"])

    def test_invalid_keyword(self):
        result = fetchTitleKeyword(123)
        self.assertEqual(result, [])

    def test_boundary_too_long_keyword(self):
        result = fetchTitleKeyword("a" * 256)
        self.assertEqual(result, [])

    def test_edge_no_matching_titles(self):
        result = fetchTitleKeyword("zzzxqv")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
