# CS3203 Fall 2026 – Best Price Book Aid

A cross-platform application that aggregates book prices from multiple online retailers, compares them, and helps users find the best available deal.

## Overview

Textbooks and required reading are expensive, and prices vary significantly between sellers. Best Price Book Aid removes the need to manually check multiple websites. Users search once, and the application compiles pricing, seller information, and historical trends to help identify the best available deal.

This project is developed by Group G for CS 3203 (Fall 2026) and follows a structured Scrum workflow.

## Table of Contents

- Features
- Architecture
- Setup and Installation
- Running Unit Tests
- Ticket 5: Sprint 1 Code Review 1-2
- Development Workflow
- Sprint Summary
- Contributing

## Features

### Price Aggregation and Search
- Search by title, author, ISBN, or keyword
- Retailer scraping from Amazon, Barnes & Noble, Bookshop, AbeBooks, and others
- API integration where available
- Price normalization for consistent comparisons

### Comparison and Insights
- Best-price algorithm to surface the lowest total cost
- Price history charts to show long-term trends
- Retailer metadata including ratings, shipping speed, and return policies

### User Interface
- Side-by-side comparisons
- Book details page with cover, description, and reviews

### Infrastructure
- Caching layer to reduce API load
- Database schema for books, retailers, prices, and history
- CI/CD pipeline for automated testing and deployment

### Security and Compliance
- Rate limiting to prevent abuse
- Compliance with scraping and API terms

## Architecture

The repository contains the following core modules:

- `search-engine/` – Book search logic
- `retailer-api-connectors/` – Retailer scraping and API integration
- `best-price-algorithm/` – Price comparison engine
- `comparison-ui/` – UI components for side-by-side comparison
- `price-history/` – Historical price tracking
- `unit-tests/` – Unit test files for individual project components

Branching follows a GitFlow structure:

- `main` – Completed sprints for deployment
- `feature` – Active development
- `release` – Preparing and merging features to complete sprints
- `hotfix` – Emergency fixes

## Setup and Installation

### Requirements

Install the following before running the application:

- [Git](https://git-scm.com/downloads)
- [Python 3.12 or newer](https://www.python.org/downloads/)

No API keys are required. Book listings load from CSV files included in the repository.

**Windows users:** Use `python` instead of `python3` in the commands below.

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/marshall-barnett/cs3203fall2026.git
cd cs3203fall2026
git checkout feature
```

### 2. Install Application Dependencies

Navigate to the application folder and install the required dependencies:

```bash
cd book-aid
pip install -r requirements.txt
```

To install development and testing tools:

```bash
pip install -r requirements-dev.txt
```

### 3. Run the Website

From inside the `book-aid/` directory:

```bash
python3 app.py
```

Open the following addresses in your browser:

- Search page: http://localhost:5000/
- API search: http://localhost:5000/api/search?q=dune
- Health check: http://localhost:5000/health

### 4. Run Application Checks

From inside the `book-aid/` directory:

```bash
ruff check .
pytest -v
```

Optional Docker commands:

```bash
docker build -t book-aid .
docker run -p 8000:8000 book-aid
```

## Running Unit Tests

Unit tests are located in the repository's `unit-tests/` directory.

### 1. Navigate to the Unit Tests Folder

From the repository root:

```bash
cd unit-tests
```

### 2. Prepare the Test Data

For tests that require the book listings CSV file:

```bash
cp ../books.csv .
```

### 3. Run All Unit Tests

```bash
PYTHONPATH=../book-aid python3 -m unittest discover -v
```

This command discovers and executes the unit tests in the `unit-tests/` directory.

### 4. Run an Individual Unit Test

To execute the Book Keyword Filter unit tests specifically:

```bash
PYTHONPATH=../book-aid python3 -m unittest test_book_keyword_filter -v
```

The test suite checks valid searches, searches with no matching results, empty inputs, duplicate results, extra spaces, capitalization, and single-book inputs.

A successful execution displays the test results followed by:

```text
Ran 8 tests

OK
```

### Unit Test Repository Links

Each student must provide a direct GitHub URL to their individual unit test file or test suite.

**Book Keyword Filter – Individual Unit Test:**

https://github.com/marshall-barnett/cs3203fall2026/blob/feature/unit-tests/test_book_keyword_filter.py

Students should provide their direct test-file URLs in the appropriate Code Review Form or activity submission.

## Ticket 5: Sprint 1 Code Review 1-2

**Objective:** Conduct a peer code review focusing on unit tests and the corresponding code functionality.

### Developer Preparation

1. Ensure the project repository includes a README with clear setup instructions.
2. The README must explain how to:
   - Clone the repository.
   - Install the required platforms and dependencies.
   - Run the application, where applicable.
   - Execute the unit tests.
3. Each student must provide a direct URL link to their individual unit test file or test suite in the repository.
4. Provide the test-file URL in the designated activity spreadsheet by inserting a hyperlink into the appropriate cell.

### Peer Code Review

The reviewer should:

1. Access the developer's unit test repository.
2. Execute the unit tests.
3. Review the test results and corresponding code functionality.
4. Document the Pass/Fail results and provide feedback using the Code Review Form.

## Development Workflow

The project follows a five-sprint release plan (September 11 – November 19, 2026). Tasks and ownership are defined in the Scrum plan.

Current task assignments include:

- Book search engine – Mark, Ford
- Retailer scraping – Daouda, Marshall
- Best price algorithm – Mohammad
- Price history – Ford

## Sprint Summary

### Sprint 1 – Price Aggregation and Search
- Book search engine
- Retailer scraping
- API integration
- Price normalization

### Sprint 2 – Comparison and Insights
- Best-price algorithm
- Price history
- Retailer metadata

### Sprint 3 – UI/UX
- Search UI
- Comparison table
- Book details page

### Sprint 4 – Infrastructure
- Database schema
- Caching layer
- CI/CD pipeline

### Sprint 5 – Security and Compliance
- Rate limiting
- Data compliance

## Contributing

1. Create a feature branch:

```bash
git checkout -b feature/<your-feature>
```

2. Commit your changes:

```bash
git add <file>
git commit -m "Describe your changes"
```

3. Push your branch:

```bash
git push origin <your-branch>
```

4. Open a pull request for review.
