"""Unit tests for the search logic in book_search.py."""

import csv

import pytest

from book_search import DATA_FILE, load_books, search_books


@pytest.fixture
def books():
    return [
        {"title": "Clean Code", "author": "Robert C. Martin", "isbn": "9780132350884", "seller": "A", "price": 29.99},
        {"title": "Clean Code", "author": "Robert C. Martin", "isbn": "9780132350884", "seller": "B", "price": 18.25},
        {"title": "Dune", "author": "Frank Herbert", "isbn": "9780441172719", "seller": "A", "price": 9.99},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "isbn": "9780547928227", "seller": "C", "price": 7.25},
    ]


def test_results_sorted_cheapest_first(books):
    prices = [b["price"] for b in search_books(books)]
    assert prices == sorted(prices)


def test_empty_query_returns_everything(books):
    assert len(search_books(books)) == len(books)


def test_title_search_is_case_insensitive(books):
    results = search_books(books, "clean CODE", field="title")
    assert len(results) == 2
    assert results[0]["seller"] == "B"  # cheapest copy first


def test_author_search(books):
    assert [b["title"] for b in search_books(books, "herbert", field="author")] == ["Dune"]


def test_isbn_search_ignores_dashes_and_spaces(books):
    assert len(search_books(books, "978-0-13-235088 4", field="isbn")) == 2


def test_isbn_search_requires_exact_match(books):
    assert search_books(books, "978013235", field="isbn") == []


def test_keyword_search_matches_all_words_across_fields(books):
    assert len(search_books(books, "clean martin")) == 2
    assert search_books(books, "clean tolkien") == []


def test_price_filters(books):
    results = search_books(books, min_price=8, max_price=20)
    assert {b["price"] for b in results} == {9.99, 18.25}


def test_no_match_returns_empty_list(books):
    assert search_books(books, "nonexistent book") == []


def test_load_books_strips_whitespace(tmp_path):
    path = tmp_path / "books.csv"
    path.write_text("title,author,isbn,seller,price\n Dune , Frank Herbert, 9780441172719 ,A, 9.99\n")
    [book] = load_books(path)
    assert book["title"] == "Dune"
    assert book["isbn"] == "9780441172719"
    assert book["price"] == 9.99


def test_real_data_file_is_valid():
    """Guards against a bad edit to books.csv breaking the live site."""
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        assert [h.strip() for h in reader.fieldnames] == ["title", "author", "isbn", "seller", "price"]
    books = load_books()
    assert books, "books.csv has no rows"
    for book in books:
        assert book["title"], f"row missing a title: {book}"
        assert book["price"] >= 0, f"negative price: {book}"
