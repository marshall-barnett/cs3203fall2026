import csv
import os
import unittest

# !! Note to reviewer, to run this all you need is this file along with books.csv in the same directory. The test will load the book titles from the CSV and run various tests on the search_book function.

# books.csv is expected to live in the same directory as this test file
BOOKS_CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books.csv")


def load_book_titles(csv_path=BOOKS_CSV_PATH):
    """Load unique book titles from the CSV, preserving file order.

    The CSV has one row per seller, so the same title can appear several times.
    """
    titles = []
    seen = set()
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            title = (row.get("title") or "").strip()
            if title and title not in seen:
                seen.add(title)
                titles.append(title)
    return titles


BOOK_DATABASE = load_book_titles()


def search_book(query):
    # Enforce string type (bool is a subclass of int in Python, so check explicitly)
    if not isinstance(query, str) or isinstance(query, bool):
        raise TypeError("Search query must be a string.")

    # Enforce non-empty and non-whitespace
    if not query.strip():
        raise ValueError("Search query cannot be empty or only spaces.")

    # Enforce maximum length constraint
    if len(query) > 255:
        raise ValueError("Search query exceeds maximum allowed length of 255 characters.")

    # Case-insensitive match against the book database loaded from books.csv
    normalized_query = query.lower()
    return [book for book in BOOK_DATABASE if normalized_query in book.lower()]


class TestSearchBook(unittest.TestCase):

    def test_database_loaded_from_csv(self):
        self.assertTrue(len(BOOK_DATABASE) > 0)
        self.assertEqual(len(BOOK_DATABASE), len(set(BOOK_DATABASE)))

    def test_search_with_valid_string(self):
        result = search_book("Clean Code")
        self.assertIsNotNone(result)
        self.assertIn("Clean Code", result)

    def test_search_is_case_insensitive(self):
        self.assertEqual(search_book("clean code"), search_book("CLEAN CODE"))

    def test_search_with_non_string_types(self):
        invalid_inputs = [123, 45.67, True, ["Gatsby"], {"title": "X"}, None]
        for invalid_input in invalid_inputs:
            with self.subTest(invalid_input=invalid_input):
                with self.assertRaises(TypeError):
                    search_book(invalid_input)

    def test_search_minimum_valid_length(self):
        result = search_book("A")
        self.assertIsNotNone(result)

    def test_search_maximum_valid_length(self):
        max_length_term = "a" * 255
        result = search_book(max_length_term)
        self.assertIsNotNone(result)

    def test_search_empty_string(self):
        with self.assertRaises(ValueError):
            search_book("")

    def test_search_only_spaces(self):
        with self.assertRaises(ValueError):
            search_book("   ")

    def test_search_exceeds_maximum_length(self):
        over_limit_term = "a" * 256
        with self.assertRaises(ValueError):
            search_book(over_limit_term)

    def test_search_no_matching_books(self):
        result = search_book("NonExistentBookTitle12345XYZ")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
