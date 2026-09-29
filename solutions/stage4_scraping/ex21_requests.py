"""
练习 21：用 requests 发送 HTTP 请求
==================================

requests 是 Python 最流行的 HTTP 库（类似 JS 的 fetch / axios，但是同步的）。

知识点
------
    import requests
    resp = requests.get(url, params={"q": "python"}, headers={...}, timeout=10)
    resp.status_code      # 200
    resp.raise_for_status()   # 4xx/5xx 时抛出 requests.HTTPError（fetch 不会自动抛错！）
    resp.text             # 文本（HTML）
    resp.json()           # 解析 JSON（类似 await res.json()）
    resp.encoding = resp.apparent_encoding   # 中文网页乱码时常用
    requests.post(url, json={...}) / data={...}

- Session：复用连接、自动保持 cookie，爬多个页面时推荐使用
      session = requests.Session()
      session.get(...)
- 异常都继承自 requests.RequestException：
      ConnectionError, Timeout, HTTPError ...
- ⚠️ 一定要设置 timeout，否则可能永远卡住
- 🧭 爬虫礼仪：设置 User-Agent、控制频率（time.sleep）、遵守 robots.txt 和网站条款

为了让测试不依赖网络，本练习的函数都把 session / fetch / sleep 作为参数传入
（这叫“依赖注入”）。测试会传入假的对象；实际使用时传入 requests.Session() 和 time.sleep 即可：

    import requests, time
    with requests.Session() as s:
        html = fetch_html("https://quotes.toscrape.com/", s)

运行测试：  pytest tests/test_ex21_requests.py
"""
import time
from urllib.parse import urlencode

import requests

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (learn-python crawler; +https://github.com/)",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def build_url(base, params):
    """把查询参数拼接到 URL 上（值为 None 的参数跳过）。
    提示：urllib.parse.urlencode

    >>> build_url("https://example.com/search", {"q": "python 爬虫", "page": 2, "sort": None})
    'https://example.com/search?q=python+%E7%88%AC%E8%99%AB&page=2'
    """
    clean = {k: v for k, v in params.items() if v is not None}
    return f"{base}?{urlencode(clean)}" if clean else base


def fetch_html(url, session, timeout=10):
    """用 session.get 获取网页：
    - 传入 headers=DEFAULT_HEADERS 和 timeout=timeout
    - 调用 raise_for_status() 检查状态码
    - 返回 resp.text
    """
    resp = session.get(url, headers=DEFAULT_HEADERS, timeout=timeout)
    resp.raise_for_status()
    return resp.text


def fetch_json(url, session, params=None, timeout=10):
    """GET 一个 JSON 接口：传 params、headers=DEFAULT_HEADERS、timeout，检查状态码后返回 resp.json()。"""
    resp = session.get(url, params=params, headers=DEFAULT_HEADERS, timeout=timeout)
    resp.raise_for_status()
    return resp.json()


def fetch_with_retry(url, session, retries=3, backoff=1.0, sleep=time.sleep):
    """调用 fetch_html，遇到 requests.RequestException 时重试。
    - 最多尝试 retries 次
    - 第 i 次失败后（i 从 0 开始）等待 backoff * 2**i 秒（指数退避），最后一次失败后不等待
    - 全部失败时重新抛出最后一次的异常
    """
    for attempt in range(retries):
        try:
            return fetch_html(url, session)
        except requests.RequestException:
            if attempt == retries - 1:
                raise
            sleep(backoff * 2 ** attempt)


def crawl_politely(urls, fetch, delay=1.0, sleep=time.sleep):
    """依次抓取 urls，返回 {url: html}：
    - 每两次请求之间调用 sleep(delay)（第一个请求前、最后一个请求后都不需要）
    - 某个 url 抓取抛出异常时，结果记为 None，继续抓取下一个
    """
    results = {}
    for i, url in enumerate(urls):
        if i > 0:
            sleep(delay)
        try:
            results[url] = fetch(url)
        except Exception:  # noqa: BLE001 - 单个页面失败不影响整体
            results[url] = None
    return results


def parse_api_users(payload):
    """从接口返回的嵌套 JSON 中提取用户信息：

    输入：{"code": 0, "data": {"users": [
              {"id": 1, "profile": {"name": "Tom", "city": "北京"}, "tags": ["a", "b"]},
              {"id": 2, "profile": {"name": "Amy"}, "tags": []}]}}
    输出：[{"id": 1, "name": "Tom", "city": "北京", "tags": "a,b"},
           {"id": 2, "name": "Amy", "city": None, "tags": ""}]

    code 不为 0 时抛出 ValueError(payload.get("message", "接口错误"))
    """
    if payload.get("code") != 0:
        raise ValueError(payload.get("message", "接口错误"))
    users = []
    for u in payload["data"]["users"]:
        profile = u.get("profile", {})
        users.append({
            "id": u["id"],
            "name": profile.get("name"),
            "city": profile.get("city"),
            "tags": ",".join(u.get("tags", [])),
        })
    return users
