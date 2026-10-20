"""Integration tests for the Flask routes in app.py."""

import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_home_page_loads(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"<form" in resp.data


def test_home_page_search_shows_results(client):
    resp = client.get("/?q=dune&field=title")
    assert resp.status_code == 200
    assert b"Dune" in resp.data


def test_api_search_returns_sorted_json(client):
    resp = client.get("/api/search?q=clean+code&field=title")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data, "expected at least one Clean Code listing"
    prices = [b["price"] for b in data]
    assert prices == sorted(prices)


def test_api_search_price_filter(client):
    data = client.get("/api/search?max_price=10").get_json()
    assert data and all(b["price"] <= 10 for b in data)


def test_api_bad_field_and_price_fall_back_safely(client):
    resp = client.get("/api/search?q=dune&field=bogus&min_price=abc")
    assert resp.status_code == 200
    assert any(b["title"] == "Dune" for b in resp.get_json())
