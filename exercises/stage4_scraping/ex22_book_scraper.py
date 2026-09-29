"""
练习 22：综合项目 —— 多页图书爬虫
================================

把前面学到的东西串起来：抓取 → 解析 → 翻页 → 清洗 → 分析 → 保存。

网站结构（本地模拟，见 data/pages/books/page-1.html ~ page-3.html，可以先用浏览器打开看看）：
    <article class="product_pod">
      <p class="star-rating Four"></p>
      <h3><a href="../book/book-3.html" title="完整书名">截断的书名...</a></h3>
      <p class="price_color">¥119.00</p>
      <p class="availability">缺货</p>
    </article>
    ...
    <li class="next"><a href="page-2.html">下一页</a></li>     # 最后一页没有 next

注意几个爬虫中常见的“坑”：
- 显示的书名可能被截断，完整书名在 title 属性里
- 评分藏在 class 名里（"star-rating Four"），需要转换成数字
- 价格带货币符号，需要转换成 float
- 链接是相对路径，需要 urljoin 成绝对地址
- 翻页要防止死循环（记录访问过的 URL，并设置最大页数）

这个练习写完后，你可以把 fetch 换成真实的 requests 请求，
去爬 https://books.toscrape.com/（专门给人练习爬虫的网站，结构几乎一样）。

运行测试：  pytest tests/test_ex22_book_scraper.py
"""
from urllib.parse import urljoin

import pandas as pd
from bs4 import BeautifulSoup

RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_price(text):
    """ "¥1,119.00" -> 1119.0（去掉货币符号、逗号和空白）"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def parse_rating(class_list):
    """["star-rating", "Four"] -> 4；找不到评分返回 0。使用 RATINGS。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def parse_books(html, page_url):
    """解析一页中的所有图书，返回 dict 列表，每个 dict：
    {"title": 完整书名, "price": float, "rating": int, "in_stock": bool, "url": 绝对地址}
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def next_page_url(html, page_url):
    """返回“下一页”的绝对地址；没有下一页返回 None。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def crawl_books(start_url, fetch, max_pages=50):
    """从 start_url 开始不断翻页抓取所有图书。
    - fetch(url) -> html，由调用者传入（测试中读取本地文件，实战中用 requests）
    - 最多抓取 max_pages 页
    - 遇到已经访问过的 URL 就停止（防止死循环）
    返回所有图书的列表。
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def books_to_dataframe(books):
    """转成 DataFrame，按 rating 降序、price 升序排序，重置索引。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError


def rating_report(df):
    """按评分统计：index 为 rating（降序），列 count（数量）、avg_price（平均价格，保留2位）、
    in_stock（有货数量，int）。
    """
    # TODO: 在这里写你的代码
    raise NotImplementedError


def save_books_csv(df, path):
    """保存为 CSV，不写索引，使用 encoding="utf-8-sig"（带 BOM，Excel 打开中文不乱码）。"""
    # TODO: 在这里写你的代码
    raise NotImplementedError
