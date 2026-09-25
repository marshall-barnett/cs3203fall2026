# cs3203fall2026
**Best Price Book Aid**

A cross‑platform application that aggregates book prices from multiple online retailers, compares them in real time, and helps users find the best available deal.

**Overview**

Textbooks and required reading are expensive, and prices vary significantly between sellers. Best Price Book Aid removes the need to manually check multiple websites. Search once, and the application compiles pricing, seller reviews, and historical trends to surface the best available deal.

This project is developed by Group G for CS 3203 (Fall 2026) and follows a structured Scrum workflow.

**Table of Contents**

- Features
- Architecture
- Installation
- Usage
- Development Workflow
- Sprint Plan
- Contributing

**Features**

**Price Aggregation and Search**

- Search by title, author, ISBN, or keyword
- Retailer scraping from Amazon, Barnes & Noble, Bookshop, AbeBooks, and others
- API integration where available
- Price normalization for consistent comparisons

**Comparison and Insights**

- Best‑price algorithm to surface the lowest total cost
- Price history charts to show long‑term trends
- Retailer metadata including ratings, shipping speed, and return policies

**User Interface**

- Side‑by‑side comparisons
- Book details page with cover, description, and reviews

**Infrastructure**

- Caching layer to reduce API load
- Database schema for books, retailers, prices, and history
- CI/CD pipeline for automated testing and deployment

**Security and Compliance**

- Rate limiting to prevent abuse
- Compliance with scraping and API terms

**Architecture**

The repository contains the following core modules:

- search-engine/ — Book search logic
- retailer-api-connectors/ — Retailer scraping and API integration
- best-price-algorithm/ — Price comparison engine
- comparison-ui/ — UI components for side‑by‑side comparison
- price-history/ — Historical price tracking

Branching follows a GitFlow structure:

- main — Completed sprints for deployment
- feature — Active development
- release — Preparing and merging features to complete sprints
- hotfix — Emergency fixes

**Installation**

Clone the repository:

git clone <https://github.com/&lt;your-org&gt;/cs3203fall2026.git>

cd cs3203fall2026

Install dependencies:

npm install

Or for Python modules:

pip install -r requirements.txt

**Usage**

Search for a book:

python search-engine/search.py --isbn 9780131103627

Run comparison:

python best-price-algorithm/compare.py --title "Operating Systems"

Launch the UI:

npm run start

**Development Workflow**

The project follows a five‑sprint release plan (Sep 11 – Nov 19, 2026). Tasks and ownership are defined in the Scrum plan, including:

"Book search engine — Mark, Ford"

"Retailer scraping — Daouda, Marshall"

"Best price algorithm — Mohammad"

"Price history — Ford"

**Sprint Summary**

**Sprint 1 — Price Aggregation and Search**

- Book search engine
- Retailer scraping
- API integration
- Price normalization

**Sprint 2 — Comparison and Insights**

- Best‑price algorithm
- Price history
- Retailer metadata

**Sprint 3 — UI/UX**

- Search UI
- Comparison table
- Book details page

**Sprint 4 — Infrastructure**

- Database schema
- Caching layer
- CI/CD pipeline

**Sprint 5 — Security and Compliance**

- Rate limiting
- Data compliance

**Contributing**

1. Create a feature branch:

git checkout -b feature/&lt;your-feature&gt;

2. Commit changes:

git commit -m "Add new feature"

3. Push and open a pull request.
