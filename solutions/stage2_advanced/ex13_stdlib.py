"""
练习 13：常用标准库（数据处理 & 爬虫都会大量用到）
===============================================

- collections
      Counter(iterable)            计数器，.most_common(n)
      defaultdict(list)            访问不存在的 key 自动创建默认值
      deque(maxlen=n)              双端队列，可限制长度
      namedtuple("Point", "x y")   带字段名的元组
- itertools：combinations, permutations, product, groupby, chain, islice
- datetime：
      from datetime import date, datetime, timedelta
      datetime.strptime("2024-01-05", "%Y-%m-%d")   字符串 -> 时间
      dt.strftime("%Y年%m月%d日")                     时间 -> 字符串
      d2 - d1 得到 timedelta，.days 取天数
      d.weekday()  周一为 0
- re（正则表达式，爬虫必备）：
      re.findall(pattern, text)   re.search()   re.sub()   re.match()
      建议用原始字符串写正则：r"\\d+"
- math, random, statistics

运行测试：  pytest tests/test_ex13_stdlib.py
"""
import math
import re
from collections import Counter, defaultdict, deque, namedtuple
from datetime import date, datetime, timedelta
from itertools import combinations


def most_common_words(text, n):
    """返回出现次数最多的 n 个单词及其次数（忽略大小写，只考虑字母组成的单词）。

    提示：re.findall(r"[a-z]+", text.lower()) 配合 Counter

    >>> most_common_words("a b a c b a", 2)
    [('a', 3), ('b', 2)]
    """
    words = re.findall(r"[a-z]+", text.lower())
    return Counter(words).most_common(n)


def group_anagrams(words):
    """把字母异位词分到一组，返回 dict：排序后的字母串 -> 单词列表。提示：defaultdict

    >>> group_anagrams(["eat", "tea", "tan", "ate", "nat"])
    {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat']}
    """
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return dict(groups)


def days_between(start, end):
    """两个 "YYYY-MM-DD" 日期字符串之间相差的天数（end - start）。

    >>> days_between("2024-01-01", "2024-03-01")
    60
    """
    fmt = "%Y-%m-%d"
    return (datetime.strptime(end, fmt) - datetime.strptime(start, fmt)).days


WEEKDAYS = ["一", "二", "三", "四", "五", "六", "日"]


def format_chinese_date(text):
    """ "2024-03-05" -> "2024年03月05日 星期二"。可使用上面的 WEEKDAYS。"""
    d = datetime.strptime(text, "%Y-%m-%d")
    return d.strftime("%Y年%m月%d日") + f" 星期{WEEKDAYS[d.weekday()]}"


def add_workdays(start, n):
    """从 start（date 对象）开始，往后数 n 个工作日（跳过周六日），返回 date。

    >>> add_workdays(date(2024, 3, 1), 1)   # 周五 + 1 个工作日 = 下周一
    datetime.date(2024, 3, 4)
    """
    current = start
    while n > 0:
        current += timedelta(days=1)
        if current.weekday() < 5:
            n -= 1
    return current


def extract_emails(text):
    """用正则提取文本中所有邮箱地址（按出现顺序）。

    >>> extract_emails("联系 a.b@test.com 或 hr@company.cn")
    ['a.b@test.com', 'hr@company.cn']
    """
    return re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", text)


def extract_prices(text):
    """提取文本中所有价格数字（可能带小数），返回 float 列表。

    >>> extract_prices("原价 ¥199.00，现价 ¥99，运费 5.5 元")
    [199.0, 99.0, 5.5]
    """
    return [float(x) for x in re.findall(r"\d+(?:\.\d+)?", text)]


def team_pairs(members):
    """返回所有两人组合（元组列表），顺序与 itertools.combinations 一致。"""
    return list(combinations(members, 2))


def last_n_events(events, n):
    """只保留最近 n 条事件，返回列表。提示：deque(maxlen=n)"""
    return list(deque(events, maxlen=n))


Point = namedtuple("Point", ["x", "y"])


def distance(p1, p2):
    """两个 Point 之间的欧几里得距离。提示：math.dist 或 math.hypot

    >>> distance(Point(0, 0), Point(3, 4))
    5.0
    """
    return math.hypot(p2.x - p1.x, p2.y - p1.y)
