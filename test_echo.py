"""
Автотесты для сервиса Postman Echo.
"""

import requests


BASE_URL = "https://postman-echo.com"
TIMEOUT = 10


def test_get_with_query_params():
    """GET /get возвращает переданные query-параметры в поле args."""
    params = {
        "foo": "bar",
        "baz": "qux",
        "number": "42",
    }

    response = requests.get(
        f"{BASE_URL}/get",
        params=params,
        timeout=TIMEOUT,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["args"] == params
    assert "url" in data
    assert "headers" in data


def test_get_with_custom_header():
    """GET /get возвращает переданные заголовки в поле headers."""
    headers = {
        "X-Test-Header": "Hello",
        "User-Agent": "pytest-postman-echo",
    }

    response = requests.get(
        f"{BASE_URL}/get",
        headers=headers,
        timeout=TIMEOUT,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["headers"]["x-test-header"] == "Hello"
    assert data["headers"]["user-agent"] == "pytest-postman-echo"


def test_post_json_body():
    """POST /post возвращает JSON-тело в поле json."""
    payload = {
        "name": "Alice",
        "age": 30,
        "active": True,
    }

    response = requests.post(
        f"{BASE_URL}/post",
        json=payload,
        timeout=TIMEOUT,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["json"] == payload
    assert data["headers"]["content-type"] == "application/json"


def test_post_form_data():
    """POST /post возвращает form-urlencoded данные в поле form."""
    form_data = {
        "username": "bob",
        "password": "secret",
    }

    response = requests.post(
        f"{BASE_URL}/post",
        data=form_data,
        timeout=TIMEOUT,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["form"] == form_data
    assert data["headers"]["content-type"] == "application/x-www-form-urlencoded"


def test_post_raw_text():
    """POST /post возвращает сырое текстовое тело в поле data."""
    text = "Hello, Postman Echo!"

    response = requests.post(
        f"{BASE_URL}/post",
        data=text,
        timeout=TIMEOUT,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["data"] == text
    assert data["form"] == {}
    assert data.get("json") is None


def test_post_query_params_and_json():
    """POST /post одновременно принимает query-параметры и JSON-тело."""
    params = {
        "source": "pytest",
        "version": "1",
    }
    payload = {
        "message": "hello",
    }

    response = requests.post(
        f"{BASE_URL}/post",
        params=params,
        json=payload,
        timeout=TIMEOUT,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["args"] == params
    assert data["json"] == payload
