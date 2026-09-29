from datetime import date

from tests.utils import load

ex = load("stage2_advanced.ex13_stdlib")


def test_most_common_words():
    assert ex.most_common_words("a b a c b a", 2) == [("a", 3), ("b", 2)]
    text = "Python is great. Python, python! Is it?"
    assert ex.most_common_words(text, 2) == [("python", 3), ("is", 2)]


def test_group_anagrams():
    assert ex.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == {
        "aet": ["eat", "tea", "ate"],
        "ant": ["tan", "nat"],
        "abt": ["bat"],
    }
    assert type(ex.group_anagrams(["a"])) is dict


def test_days_between():
    assert ex.days_between("2024-01-01", "2024-03-01") == 60  # 2024 是闰年
    assert ex.days_between("2023-01-01", "2023-03-01") == 59
    assert ex.days_between("2024-01-10", "2024-01-01") == -9


def test_format_chinese_date():
    assert ex.format_chinese_date("2024-03-05") == "2024年03月05日 星期二"
    assert ex.format_chinese_date("2024-03-10") == "2024年03月10日 星期日"


def test_add_workdays():
    assert ex.add_workdays(date(2024, 3, 1), 1) == date(2024, 3, 4)
    assert ex.add_workdays(date(2024, 3, 4), 5) == date(2024, 3, 11)
    assert ex.add_workdays(date(2024, 3, 4), 0) == date(2024, 3, 4)


def test_extract_emails():
    text = "联系 a.b@test.com 或 hr@company.cn，不是邮箱: @foo, bar@"
    assert ex.extract_emails(text) == ["a.b@test.com", "hr@company.cn"]


def test_extract_prices():
    assert ex.extract_prices("原价 ¥199.00，现价 ¥99，运费 5.5 元") == [199.0, 99.0, 5.5]
    assert ex.extract_prices("免费") == []


def test_team_pairs():
    assert ex.team_pairs(["A", "B", "C"]) == [("A", "B"), ("A", "C"), ("B", "C")]


def test_last_n_events():
    assert ex.last_n_events(range(10), 3) == [7, 8, 9]
    assert ex.last_n_events([1], 3) == [1]


def test_distance():
    assert ex.distance(ex.Point(0, 0), ex.Point(3, 4)) == 5.0
    assert ex.Point(1, 2).x == 1
