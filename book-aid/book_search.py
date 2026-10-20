"""Core search logic for Best Price Book Aid (no UI code here)."""

import csv
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books.csv")


def load_books(path=DATA_FILE):
    """Read listings from the CSV file into a list of dicts."""
    books = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, skipinitialspace=True):
            row = {k.strip(): (v or "").strip() for k, v in row.items()}
            row["price"] = float(row["price"])
            books.append(row)
    return books


def search_books(books, query="", field="keyword", min_price=None, max_price=None):
    """Return listings matching the query, sorted cheapest first.

    field: "title", "author", "isbn", or "keyword" (searches all three).
    """
    query = query.strip().lower()
    results = []

    for book in books:
        if query:
            if field == "title":
                match = query in book["title"].lower()
            elif field == "author":
                match = query in book["author"].lower()
            elif field == "isbn":
                clean = query.replace("-", "").replace(" ", "")
                match = clean == book["isbn"]
            else:
                text = f'{book["title"]} {book["author"]} {book["isbn"]}'.lower()
                match = all(word in text for word in query.split())
            if not match:
                continue

        if min_price is not None and book["price"] < min_price:
            continue
        if max_price is not None and book["price"] > max_price:
            continue

        results.append(book)

    return sorted(results, key=lambda b: b["price"])
