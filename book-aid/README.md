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
3. **Deploy to staging**: on pushes to `feature`, if steps 1 and 2 pass.
4. **Deploy to Render (production)**: only on pushes to `main`, and only if steps 1 and 2 pass.

So with GitFlow: work on `feature` and check it on the staging server, merge to `release`,
then merge `release` into `main` to ship.
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

### Staging server

A second Render service, `best-price-book-aid-staging`, runs the `feature` branch so changes
can be tried on a real server before they reach `main`. One-time setup:

1. In Render, **New > Web Service**, pick this repo, and use the same settings as production
   but with **Branch** `feature` and **Auto-Deploy** off (or let the Blueprint create it from `render.yaml`).
2. Copy that service's **Deploy Hook** URL.
3. In GitHub **Settings > Secrets and variables > Actions**:
   - **Secrets**: add `RENDER_STAGING_DEPLOY_HOOK_URL` with the staging hook URL.
   - **Variables**: add `RENDER_STAGING_APP_URL` with the staging site address.
4. Push to `feature`. The **Deploy to staging** job runs after tests pass.

Free-tier note: the site sleeps after ~15 minutes idle and takes about a minute to wake on the next visit.

Other hosts also work: the `Procfile` suits Railway/Heroku, and the `Dockerfile` runs anywhere
(`docker build -t book-aid . && docker run -p 8000:8000 book-aid`).

## Endpoints

- `/` search page
- `/api/search?q=dune&field=title&max_price=12` JSON results
- `/health` health check

Replace `books.csv` with your scraped data (columns: title, author, isbn, seller, price).
