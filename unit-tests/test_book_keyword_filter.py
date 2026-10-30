
import unittest
from book_search import search_books


class TestBookKeywordFilter(unittest.TestCase):

    def test_valid_keyword(self):
        books = [
            {"title": "Software Engineering", "author": "Ian Sommerville",
             "isbn": "123456", "price": 45.00},
            {"title": "Introduction to Algorithms", "author": "Thomas Cormen",
             "isbn": "789012", "price": 65.00}
        ]
        result = search_books(books, "Software")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Software Engineering")

    def test_no_matching_books(self):
        books = [
            {"title": "Software Engineering", "author": "Ian Sommerville",
             "isbn": "123456", "price": 45.00},
            {"title": "Introduction to Algorithms", "author": "Thomas Cormen",
             "isbn": "789012", "price": 65.00}
        ]
        result = search_books(books, "Biology")
        self.assertEqual(result, [])

    def test_empty_keyword(self):
        books = [
            {"title": "Software Engineering", "author": "Ian Sommerville",
             "isbn": "123456", "price": 45.00}
        ]
        result = search_books(books, "")
        self.assertEqual(len(result), 1)

    def test_empty_book_list(self):
        result = search_books([], "Software")
        self.assertEqual(result, [])

    def test_duplicate_matching_books(self):
        books = [
            {"title": "Software Engineering", "author": "Ian Sommerville",
             "isbn": "123456", "price": 45.00},
            {"title": "Software Engineering", "author": "Ian Sommerville",
             "isbn": "123456", "price": 45.00}
        ]
        result = search_books(books, "Software")
        self.assertEqual(len(result), 2)

    def test_extra_spaces(self):
        books = [
            {"title": "Software Engineering", "author": "Ian Sommerville",
             "isbn": "123456", "price": 45.00}
        ]
        result = search_books(books, "  Software  ")
        self.assertEqual(len(result), 1)

    def test_different_capitalization(self):
        books = [
            {"title": "Software Engineering", "author": "Ian Sommerville",
             "isbn": "123456", "price": 45.00}
        ]
        result = search_books(books, "SOFTWARE")
        self.assertEqual(len(result), 1)

    def test_single_book(self):
        books = [
            {"title": "Software Engineering", "author": "Ian Sommerville",
             "isbn": "123456", "price": 45.00}
        ]
        result = search_books(books, "Software")
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
