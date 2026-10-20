# Best Price Book Aid

A small Flask app that searches book listings (from `books.csv`) and shows the cheapest first.

## Run locally

    pip install -r requirements.txt
    python app.py          # http://localhost:5000

## Deploy

**Render / Railway / Heroku (easiest):** push this folder to a GitHub repo, create a new
Web Service from it. Build command: `pip install -r requirements.txt`.
Start command: `gunicorn app:app --bind 0.0.0.0:$PORT` (the `Procfile` already has this).

**Docker (any VPS, Fly.io, Cloud Run):**

    docker build -t book-aid .
    docker run -p 8000:8000 book-aid

**Plain Linux VPS:** `pip install -r requirements.txt`, then run
`gunicorn app:app --bind 0.0.0.0:8000` behind nginx (or Caddy) for HTTPS.

## Endpoints

- `/` search page
- `/api/search?q=dune&field=title&max_price=12` JSON results
- `/health` health check

Replace `books.csv` with your scraped data (columns: title, author, isbn, seller, price).
