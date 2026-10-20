"""Best Price Book Aid - mock search.

Loads book listings from books.csv (stand-in for scraped data) and
searches by title, author, ISBN, or keyword, with an optional price range.
Results are sorted cheapest first.
"""

import csv

import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books.csv")


def load_books(path=DATA_FILE):
    """Read listings from the CSV file into a list of dicts."""
    books = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["price"] = float(row["price"])
            books.append(row)
    return books


def search_books(books, query="", field="keyword", min_price=None, max_price=None):
    """Return listings matching the query, sorted by price.

    field: "title", "author", "isbn", or "keyword" (searches all three).
    min_price / max_price: optional price limits.
    """
    query = query.strip().lower()
    results = []

    for book in books:
        # Text match
        if query:
            if field == "title":
                match = query in book["title"].lower()
            elif field == "author":
                match = query in book["author"].lower()
            elif field == "isbn":
                # ignore dashes/spaces so 978-0-13... still matches
                clean = query.replace("-", "").replace(" ", "")
                match = clean == book["isbn"]
            else:  # keyword
                text = f'{book["title"]} {book["author"]} {book["isbn"]}'.lower()
                match = all(word in text for word in query.split())
            if not match:
                continue

        # Price filter
        if min_price is not None and book["price"] < min_price:
            continue
        if max_price is not None and book["price"] > max_price:
            continue

        results.append(book)

    return sorted(results, key=lambda b: b["price"])


def print_results(results):
    if not results:
        print("No books found.")
        return
    print(f'{"Title":<42} {"Author":<22} {"Seller":<15} {"Price":>8}')
    print("-" * 90)
    for b in results:
        print(f'{b["title"][:41]:<42} {b["author"][:21]:<22} {b["seller"]:<15} ${b["price"]:>7.2f}')


def read_price(prompt):
    text = input(prompt).strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        print("  Not a number, ignoring.")
        return None


def main():
    books = load_books()
    print("Best Price Book Aid - Search")
    while True:
        print("\nSearch by: 1) Title  2) Author  3) ISBN  4) Keyword  5) Price only  q) Quit")
        choice = input("> ").strip().lower()
        if choice == "q":
            break
        fields = {"1": "title", "2": "author", "3": "isbn", "4": "keyword", "5": "keyword"}
        if choice not in fields:
            print("Pick 1-5 or q.")
            continue

        query = "" if choice == "5" else input("Search for: ")
        min_price = read_price("Min price (Enter to skip): ")
        max_price = read_price("Max price (Enter to skip): ")

        print()
        print_results(search_books(books, query, fields[choice], min_price, max_price))


if __name__ == "__main__":
    main()
