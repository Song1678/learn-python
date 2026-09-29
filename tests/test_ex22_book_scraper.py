from pathlib import Path
from urllib.parse import urlparse

import pandas as pd
import pytest

from tests.utils import DATA, load

ex = load("stage4_scraping.ex22_book_scraper")
BOOKS_DIR = DATA / "pages" / "books"
START = "https://books.example.com/catalogue/page-1.html"


def local_fetch(url):
    """假的 fetch：根据 URL 中的文件名读取本地 HTML。"""
    local_fetch.calls.append(url)
    return (BOOKS_DIR / Path(urlparse(url).path).name).read_text(encoding="utf-8")


@pytest.fixture(autouse=True)
def reset_calls():
    local_fetch.calls = []


def test_parse_price():
    assert ex.parse_price("¥119.00") == 119.0
    assert ex.parse_price(" ¥1,119.50 ") == 1119.5


def test_parse_rating():
    assert ex.parse_rating(["star-rating", "Four"]) == 4
    assert ex.parse_rating(["star-rating", "One"]) == 1
    assert ex.parse_rating(["star-rating"]) == 0


def test_parse_books():
    html = (BOOKS_DIR / "page-1.html").read_text(encoding="utf-8")
    books = ex.parse_books(html, START)
    assert len(books) == 5
    assert books[2] == {
        "title": "利用Python进行数据分析",
        "price": 119.0,
        "rating": 4,
        "in_stock": False,
        "url": "https://books.example.com/book/book-3.html",
    }
    assert books[3]["title"] == "Python网络爬虫权威指南", "完整书名在 title 属性里"


def test_next_page_url():
    p1 = (BOOKS_DIR / "page-1.html").read_text(encoding="utf-8")
    p3 = (BOOKS_DIR / "page-3.html").read_text(encoding="utf-8")
    assert ex.next_page_url(p1, START) == "https://books.example.com/catalogue/page-2.html"
    assert ex.next_page_url(p3, "https://books.example.com/catalogue/page-3.html") is None


def test_crawl_books():
    books = ex.crawl_books(START, local_fetch)
    assert len(books) == 12
    assert local_fetch.calls == [
        "https://books.example.com/catalogue/page-1.html",
        "https://books.example.com/catalogue/page-2.html",
        "https://books.example.com/catalogue/page-3.html",
    ]
    assert books[-1]["title"] == "SQL必知必会"


def test_crawl_books_max_pages():
    books = ex.crawl_books(START, local_fetch, max_pages=2)
    assert len(books) == 10
    assert len(local_fetch.calls) == 2


def test_crawl_books_stops_on_loop():
    looping = '<article class="product_pod"><p class="star-rating Two"></p>' \
              '<h3><a href="b.html" title="循环之书">循环</a></h3>' \
              '<p class="price_color">¥1.00</p><p class="availability">有货</p></article>' \
              '<li class="next"><a href="loop.html">下一页</a></li>'
    calls = []

    def fetch(url):
        calls.append(url)
        return looping

    books = ex.crawl_books("https://x.com/loop.html", fetch)
    assert len(calls) == 1
    assert len(books) == 1


# (书名, 价格, 评分, 是否有货)：与 data/pages/books 中的 12 本书一致，
# 这样即使 crawl_books 还没写完，也能单独测试后面的函数
BOOKS = [
    ("Python编程：从入门到实践", 89.0, 5, True), ("流畅的Python", 139.0, 5, True),
    ("利用Python进行数据分析", 119.0, 4, False), ("Python网络爬虫权威指南", 79.0, 3, True),
    ("深入浅出Pandas", 99.0, 4, True), ("NumPy数据处理详解", 69.5, 2, True),
    ("算法图解", 49.0, 4, False), ("JavaScript高级程序设计", 129.0, 5, True),
    ("Effective Python", 79.0, 4, True), ("Python Cookbook", 108.0, 3, True),
    ("统计学习方法", 98.0, 5, False), ("SQL必知必会", 39.0, 1, True),
]


@pytest.fixture
def books():
    return [
        {"title": t, "price": p, "rating": r, "in_stock": s, "url": f"https://books.example.com/book/book-{i}.html"}
        for i, (t, p, r, s) in enumerate(BOOKS, 1)
    ]


@pytest.fixture
def df(books):
    frame = pd.DataFrame(books)
    return frame.sort_values(["rating", "price"], ascending=[False, True]).reset_index(drop=True)


def test_books_to_dataframe(books):
    df = ex.books_to_dataframe(books)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["title", "price", "rating", "in_stock", "url"]
    assert df["title"].tolist()[:4] == ["Python编程：从入门到实践", "统计学习方法", "JavaScript高级程序设计", "流畅的Python"]
    assert df["title"].iloc[-1] == "SQL必知必会"
    assert list(df.index) == list(range(12))


def test_rating_report(df):
    report = ex.rating_report(df)
    assert report.index.tolist() == [5, 4, 3, 2, 1]
    assert report.loc[5, "count"] == 4
    assert report.loc[4, "avg_price"] == pytest.approx(86.5)
    assert report.loc[4, "in_stock"] == 2
    assert report["count"].sum() == 12


def test_save_books_csv(df, tmp_path):
    out = tmp_path / "books.csv"
    ex.save_books_csv(df, out)
    raw = out.read_bytes()
    assert raw.startswith(b"\xef\xbb\xbf"), "请使用 utf-8-sig 编码"
    loaded = pd.read_csv(out, encoding="utf-8-sig")
    assert loaded.shape == (12, 5)
    assert loaded["title"].iloc[0] == df["title"].iloc[0]
