"""Best Price Book Cat - web app."""

import os

from flask import Flask, jsonify, render_template, request

from book_search import load_books, search_books

app = Flask(__name__)
BOOKS = load_books()

FIELDS = {"title", "author", "isbn", "keyword"}


def parse_price(value):
    try:
        return float(value) if value not in (None, "") else None
    except ValueError:
        return None


def run_search():
    query = request.args.get("q", "")
    field = request.args.get("field", "keyword")
    if field not in FIELDS:
        field = "keyword"
    min_price = parse_price(request.args.get("min_price"))
    max_price = parse_price(request.args.get("max_price"))
    results = search_books(BOOKS, query, field, min_price, max_price)
    return results, query, field


@app.route("/")
def index():
    searched = any(k in request.args for k in ("q", "min_price", "max_price"))
    results, query, field = run_search() if searched else ([], "", "keyword")
    return render_template(
        "index.html",
        results=results,
        searched=searched,
        q=query,
        field=field,
        min_price=request.args.get("min_price", ""),
        max_price=request.args.get("max_price", ""),
    )


@app.route("/api/search")
def api_search():
    results, _, _ = run_search()
    return jsonify(results)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
