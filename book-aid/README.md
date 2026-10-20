# Best Price Book Aid

A small Flask app that searches book listings (from `books.csv`) and shows the cheapest first.

## Run locally

    pip install -r requirements.txt
    python app.py          # http://localhost:5000

## Run the tests

    pip install -r requirements-dev.txt
    ruff check .
    pytest -v

## CI/CD

`.github/workflows/ci-cd.yml` runs on every push and pull request to `main`, `release`, `feature` and `hotfix`:

1. **Lint and test**: `ruff check` and `pytest`.
2. **Docker build check**: builds the image, starts it, and confirms `/health` responds.
3. **Deploy to Render**: only on pushes to `main`, and only if steps 1 and 2 pass.

So with GitFlow: work on `feature`, merge to `release`, then merge `release` into `main` to ship.
A failing test blocks the deploy, and the live site keeps running the last good version.

## Deployment (Render, free tier)

One-time setup (one teammate does this):

1. Sign in at render.com with GitHub. Choose **New > Blueprint** and pick this repo.
   Render reads `render.yaml` and creates the `best-price-book-aid` web service from `main`.
2. In the service, open **Settings > Deploy Hook** and copy the URL.
3. In GitHub, go to **Settings > Secrets and variables > Actions**:
   - **Secrets** tab: add `RENDER_DEPLOY_HOOK_URL` with the hook URL.
   - **Variables** tab: add `RENDER_APP_URL` with the site address (e.g. `https://best-price-book-aid.onrender.com`).
4. Push or merge to `main`. Watch the run in the **Actions** tab.

Free-tier note: the site sleeps after ~15 minutes idle and takes about a minute to wake on the next visit.

Other hosts also work: the `Procfile` suits Railway/Heroku, and the `Dockerfile` runs anywhere
(`docker build -t book-aid . && docker run -p 8000:8000 book-aid`).

## Endpoints

- `/` search page
- `/api/search?q=dune&field=title&max_price=12` JSON results
- `/health` health check

Replace `books.csv` with your scraped data (columns: title, author, isbn, seller, price).
