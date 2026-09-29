import pytest

from tests.utils import DATA, load

ex = load("stage4_scraping.ex20_html_parsing")
BASE = "https://blog.example.com/posts/python-crawler.html"


@pytest.fixture(scope="module")
def html():
    return (DATA / "pages" / "article.html").read_text(encoding="utf-8")


def test_get_title(html):
    assert ex.get_title(html) == "Python 爬虫入门指南 - 技术博客"
    assert ex.get_title("<html><body></body></html>") is None


def test_get_meta(html):
    assert ex.get_meta(html, "description") == "从零开始学习 Python 网络爬虫"
    assert ex.get_meta(html, "keywords").split(",") == ["Python", "爬虫", "BeautifulSoup", "requests"]
    assert ex.get_meta(html, "author") is None


def test_extract_headings(html):
    assert ex.extract_headings(html) == [
        ("h1", "Python 爬虫入门指南"),
        ("h2", "一、准备工作"),
        ("h3", "1.1 安装依赖"),
        ("h2", "二、城市数据示例"),
        ("h2", "三、注意事项"),
    ]


def test_extract_links(html):
    assert ex.extract_links(html, BASE) == [
        "https://blog.example.com/",
        "https://blog.example.com/posts/",
        "https://pypi.org/project/requests/",
        "https://pypi.org/project/beautifulsoup4/",
        "https://blog.example.com/posts/scrapy.html",
    ]


def test_get_author_and_date(html):
    assert ex.get_author_and_date(html) == {"author": "小码", "date": "2024-05-20"}


def test_texts_by_selector(html):
    assert ex.texts_by_selector(html, "ul.rules li.tip") == ["遵守 robots.txt", "控制访问频率"]
    assert ex.texts_by_selector(html, ".tip") == ["建议使用虚拟环境。", "遵守 robots.txt", "控制访问频率"]
    assert ex.texts_by_selector(html, ".nothing") == []


def test_parse_table(html):
    rows = ex.parse_table(html, "cities")
    assert rows == [
        {"城市": "北京", "人口（万）": "2185", "面积（km²）": "16410"},
        {"城市": "上海", "人口（万）": "2487", "面积（km²）": "6340"},
        {"城市": "深圳", "人口（万）": "1768", "面积（km²）": "1997"},
    ]
    assert ex.parse_table(html, "other") == [{"x": "1"}]
