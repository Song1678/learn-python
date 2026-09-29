import pytest
import requests

from tests.utils import load

ex = load("stage4_scraping.ex21_requests")


class FakeResponse:
    def __init__(self, text="", status_code=200, json_data=None):
        self.text = text
        self.status_code = status_code
        self._json = json_data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code} Error")

    def json(self):
        return self._json


class FakeSession:
    """记录每次 get 调用，并按顺序返回预设的响应（或抛出预设的异常）。"""

    def __init__(self, *responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        result = self.responses.pop(0)
        if isinstance(result, Exception):
            raise result
        return result


def test_build_url():
    url = ex.build_url("https://example.com/search", {"q": "python 爬虫", "page": 2, "sort": None})
    assert url == "https://example.com/search?q=python+%E7%88%AC%E8%99%AB&page=2"
    assert ex.build_url("https://example.com/", {}) == "https://example.com/"


def test_fetch_html():
    session = FakeSession(FakeResponse("<h1>hi</h1>"))
    assert ex.fetch_html("https://a.com", session, timeout=5) == "<h1>hi</h1>"
    url, kwargs = session.calls[0]
    assert url == "https://a.com"
    assert kwargs["timeout"] == 5
    assert kwargs["headers"] == ex.DEFAULT_HEADERS


def test_fetch_html_http_error():
    with pytest.raises(requests.HTTPError):
        ex.fetch_html("https://a.com/404", FakeSession(FakeResponse(status_code=404)))


def test_fetch_json():
    session = FakeSession(FakeResponse(json_data={"ok": True}))
    assert ex.fetch_json("https://api.com/x", session, params={"page": 1}) == {"ok": True}
    _, kwargs = session.calls[0]
    assert kwargs["params"] == {"page": 1}
    assert kwargs["headers"] == ex.DEFAULT_HEADERS
    assert "timeout" in kwargs


def test_fetch_with_retry_success():
    session = FakeSession(requests.ConnectionError("断网"), FakeResponse(status_code=503), FakeResponse("ok"))
    sleeps = []
    assert ex.fetch_with_retry("https://a.com", session, retries=3, backoff=0.5, sleep=sleeps.append) == "ok"
    assert sleeps == [0.5, 1.0]
    assert len(session.calls) == 3


def test_fetch_with_retry_gives_up():
    session = FakeSession(requests.Timeout("1"), requests.Timeout("2"), requests.Timeout("3"))
    sleeps = []
    with pytest.raises(requests.Timeout, match="3"):
        ex.fetch_with_retry("https://a.com", session, retries=3, backoff=1, sleep=sleeps.append)
    assert sleeps == [1, 2], "最后一次失败后不应再等待"


def test_crawl_politely():
    sleeps = []

    def fetch(url):
        if "bad" in url:
            raise requests.ConnectionError("boom")
        return f"<html>{url}</html>"

    urls = ["https://a.com/1", "https://a.com/bad", "https://a.com/3"]
    result = ex.crawl_politely(urls, fetch, delay=2, sleep=sleeps.append)
    assert result == {
        "https://a.com/1": "<html>https://a.com/1</html>",
        "https://a.com/bad": None,
        "https://a.com/3": "<html>https://a.com/3</html>",
    }
    assert sleeps == [2, 2]


def test_parse_api_users():
    payload = {"code": 0, "data": {"users": [
        {"id": 1, "profile": {"name": "Tom", "city": "北京"}, "tags": ["a", "b"]},
        {"id": 2, "profile": {"name": "Amy"}, "tags": []},
    ]}}
    assert ex.parse_api_users(payload) == [
        {"id": 1, "name": "Tom", "city": "北京", "tags": "a,b"},
        {"id": 2, "name": "Amy", "city": None, "tags": ""},
    ]
    with pytest.raises(ValueError, match="token 过期"):
        ex.parse_api_users({"code": 401, "message": "token 过期"})
