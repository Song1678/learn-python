"""
练习 20：用 BeautifulSoup 解析 HTML
==================================

爬虫 = 获取网页（requests） + 解析网页（BeautifulSoup） + 保存数据（csv / pandas / 数据库）。
这一练习只练“解析”，数据来自本地文件 data/pages/article.html（建议先用浏览器打开看看）。

知识点（对 JS 开发者来说很熟悉，类似 DOM API）
------------------------------------------
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    soup.title.string                 # <title> 的文本
    soup.find("h1")                   # 第一个匹配，类似 querySelector；找不到返回 None
    soup.find_all("a")                # 所有匹配，类似 querySelectorAll
    soup.find("meta", attrs={"name": "description"})
    soup.find_all(["h1", "h2"])       # 多种标签
    soup.find_all("li", class_="tip") # class 是 Python 关键字，所以写 class_

    soup.select("ul.rules > li")      # CSS 选择器！和 querySelectorAll 一样
    soup.select_one("#cities")        # 和 querySelector 一样

    tag.get_text(strip=True)          # 文本内容，类似 textContent
    tag["href"] / tag.get("href")     # 属性，类似 getAttribute
    tag.name                          # 标签名，如 "h2"

- 相对链接转绝对链接：  urllib.parse.urljoin(base_url, href)
      urljoin("https://a.com/blog/post.html", "../img/x.png") -> "https://a.com/img/x.png"

运行测试：  pytest tests/test_ex20_html_parsing.py
"""
from urllib.parse import urljoin

from bs4 import BeautifulSoup


def get_title(html):
    """返回 <title> 的文本（去掉首尾空白）；没有 title 返回 None。"""
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.get_text(strip=True) if soup.title else None


def get_meta(html, name):
    """返回 <meta name="..."> 的 content 属性；不存在返回 None。"""
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find("meta", attrs={"name": name})
    return tag.get("content") if tag else None


def extract_headings(html):
    """按文档顺序提取所有 h1/h2/h3，返回 [(标签名, 文本), ...]。"""
    soup = BeautifulSoup(html, "html.parser")
    return [(tag.name, tag.get_text(strip=True)) for tag in soup.find_all(["h1", "h2", "h3"])]


def extract_links(html, base_url):
    """提取所有 <a href> 链接并转为绝对地址：
    - 跳过以 "#"、"javascript:"、"mailto:" 开头的链接
    - 去重，保留第一次出现的顺序
    """
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("#", "javascript:", "mailto:")):
            continue
        url = urljoin(base_url, href)
        if url not in links:
            links.append(url)
    return links


def get_author_and_date(html):
    """返回 {"author": 作者名, "date": <time> 标签的 datetime 属性}。
    提示：CSS 选择器 "p.meta .author" 和 "time"
    """
    soup = BeautifulSoup(html, "html.parser")
    return {
        "author": soup.select_one("p.meta .author").get_text(strip=True),
        "date": soup.select_one("time")["datetime"],
    }


def texts_by_selector(html, selector):
    """返回 CSS 选择器匹配到的所有元素的文本列表（strip 过）。"""
    soup = BeautifulSoup(html, "html.parser")
    return [tag.get_text(strip=True) for tag in soup.select(selector)]


def parse_table(html, table_id):
    """把 id 为 table_id 的表格解析为 dict 列表：表头 <th> 为 key，单元格文本（strip 过）为 value。

    >>> # [{"城市": "北京", "人口（万）": "2185", ...}, ...]
    """
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", id=table_id)
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr"):
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if cells:
            rows.append(dict(zip(headers, cells)))
    return rows
